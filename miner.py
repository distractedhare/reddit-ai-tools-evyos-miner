import requests
import json
from datetime import datetime
import os

# Config
SUBREDDITS = ['LocalLLaMA', 'MachineLearning', 'artificial', 'OpenAI', 'singularity', 'ChatGPT', 'AI', 'LLM', 'StableDiffusion', 'PromptEngineering', 'aiagents', 'ClaudeAI']
KEYWORDS = ['tool', 'app', 'library', 'framework', 'released', 'launch', 'alternative', 'resource', 'tutorial', 'guide', 'OSS', 'github', 'demo']

def fetch_reddit_new(sub):
    url = f'https://www.reddit.com/r/{sub}/new.json?limit=20'
    headers = {'User-Agent': 'EvyOS-AI-Miner/1.0'}
    try:
        r = requests.get(url, headers=headers)
        return r.json()['data']['children'] if r.ok else []
    except:
        return []

def is_ai_tool_post(post):
    title = post['data']['title'].lower()
    selftext = post['data'].get('selftext', '').lower()
    score = post['data']['score']
    if score < 5: return False
    if any(k in title or k in selftext for k in KEYWORDS):
        return True
    return False

def extract_info(post):
    d = post['data']
    return {
        'title': d['title'],
        'url': 'https://reddit.com' + d['permalink'],
        'subreddit': d['subreddit'],
        'score': d['score'],
        'created': datetime.fromtimestamp(d['created_utc']).isoformat(),
        'link': d.get('url', ''),
        'excerpt': (d.get('selftext', '')[:200] or 'No body'),
        'flair': d.get('link_flair_text', ''),
        'suggested_name': d['title'][:60] + '...' if len(d['title']) > 60 else d['title']
    }

discoveries = []
for sub in SUBREDDITS:
    posts = fetch_reddit_new(sub)
    for p in posts:
        if is_ai_tool_post(p):
            info = extract_info(p)
            discoveries.append(info)

# Dedup simple + sort
# (add seen set later)
discoveries = sorted(discoveries, key=lambda x: x['score'], reverse=True)[:10]  # top 10 per run

print(json.dumps(discoveries, indent=2))

# Save outputs
with open('discoveries.json', 'w') as f:
    json.dump(discoveries, f)

# For CSV (EvyOS import)
with open('ai_discoveries.csv', 'w') as f:
    f.write('Title,URL,Subreddit,Score,Date,Excerpt,Import to EvyOS
')
    for d in discoveries:
        f.write(f'"{d["title"]}","{d["url"]}","{d["subreddit"]}",{d["score"]},"{d["created"]}","{d["excerpt"]}","Add as Task/Project in AI Radar"
')

print('✅ Mined', len(discoveries), 'potential AI gems! Ready for EvyOS.')