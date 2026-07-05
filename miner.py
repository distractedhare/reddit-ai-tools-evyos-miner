import requests
import os
from datetime import datetime

# Combined Reddit + HN + X (optional) hourly miner for direct EvyOS paste
# X requires free Bearer Token from developer.x.com (app-only, basic search is free)

SUBREDDITS = ['LocalLLaMA', 'MachineLearning', 'artificial', 'OpenAI', 'singularity', 'aiagents']
KEYWORDS = ['tool', 'app', 'library', 'launched', 'released', 'framework', 'agent', 'resource', 'github']

HN_KEYWORDS = ['ai', 'tool', 'llm', 'agent', 'launched', 'framework', 'library', 'show hn']

X_QUERY = '(AI OR LLM OR agent) (tool OR app OR library OR framework OR launched OR "open source" OR github) min_faves:2 -is:retweet'


def fetch_reddit():
    discoveries = []
    for sub in SUBREDDITS:
        try:
            data = requests.get(f'https://www.reddit.com/r/{sub}/new.json?limit=8', headers={'User-Agent': 'EvyOSMiner/1.0'}).json()
            for child in data.get('data', {}).get('children', []):
                p = child.get('data', {})
                title = p.get('title', '').lower()
                if any(k in title for k in KEYWORDS) and p.get('score', 0) > 8:
                    discoveries.append(f'• Reddit r/{sub}: {p["title"]} | https://reddit.com{p["permalink"]} | Paste as Task: "Explore {p["title"][:45]} (link in notes)"')
        except:
            pass
    return discoveries[:6] or ['No fresh Reddit gems this hour.']


def fetch_hn():
    try:
        ids = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json').json()[:25]
        posts = []
        for iid in ids:
            try:
                item = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{iid}.json').json() or {}
                if item.get('type') == 'story' and item.get('title'):
                    title_l = item['title'].lower()
                    if any(k in title_l for k in HN_KEYWORDS) and item.get('score', 0) > 4:
                        posts.append(f'• HN: {item["title"]} | https://news.ycombinator.com/item?id={iid} | Paste as Task: "Check this HN tool: {item["title"][:40]}"')
            except:
                pass
        return posts[:5] or ['No standout HN tools right now.']
    except:
        return ['HN API hiccup - try again later.']


def fetch_x():
    token = os.getenv('X_BEARER_TOKEN')
    if not token:
        return ['X: Add X_BEARER_TOKEN secret (free at developer.x.com) for live X monitoring of new AI tools.']
    headers = {'Authorization': f'Bearer {token}'}
    url = f'https://api.twitter.com/2/tweets/search/recent?query={X_QUERY}&max_results=5&tweet.fields=created_at,text,public_metrics&expansions=author_id&user.fields=username'
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code != 200:
            return [f'X API note: {r.status_code} (check token/rate limit)']
        data = r.json()
        posts = []
        if 'data' in data:
            users = {u['id']: u['username'] for u in data.get('includes', {}).get('users', [])}
            for t in data['data']:
                uname = users.get(t.get('author_id'), 'x')
                txt = t.get('text', '')[:120].replace('\n', ' ')
                url = f'https://x.com/{uname}/status/{t["id"] }'
                posts.append(f'• X @{uname}: {txt}... | {url} | Paste as Task: "Check X tool from @{uname}"')
        return posts[:4] or ['No high-signal X posts this hour.']
    except Exception as e:
        return [f'X fetch error: {str(e)[:60]}']


# Build the direct-paste block for EvyOS
reddit_posts = fetch_reddit()
hn_posts = fetch_hn()
x_posts = fetch_x()

paste_block = f'''🚀 EvyOS AI Tools Radar - Hourly Digest ({datetime.now().strftime("%Y-%m-%d %H:%M")})

Copy EVERYTHING below this line and paste into your EvyOS "AI Tools Radar" Project / Note / Tasks:

=== FROM X (Twitter) ===
{chr(10).join(x_posts)}

=== FROM HACKER NEWS ===
{chr(10).join(hn_posts)}

=== FROM REDDIT ===
{chr(10).join(reddit_posts)}

---
Tip: Add promising ones as Tasks with the link in notes. Review weekly in EvyOS.
Your personal AI gold miner is running! Reply to digest or here to tweak keywords/subs.''' 

print(paste_block)
print('\n\n✅ Digest ready - paste directly into EvyOS for zero-friction feed.')

# Optional: save to file for artifact
with open('evyos_ai_digest.txt', 'w') as f:
    f.write(paste_block)
