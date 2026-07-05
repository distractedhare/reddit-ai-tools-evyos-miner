import requests
import json
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Ultra-simple direct-to-EvyOS via email
SUBREDDITS = ['LocalLLaMA', 'MachineLearning', 'artificial', 'OpenAI', 'singularity']
KEYWORDS = ['tool','app','library','launched','released','resource']

def mine():
    discoveries = []
    for sub in SUBREDDITS:
        data = requests.get(f'https://www.reddit.com/r/{sub}/new.json?limit=10', headers={'User-Agent': 'EvyOSMiner'}).json()
        for child in data['data']['children']:
            p = child['data']
            if any(k in p['title'].lower() for k in KEYWORDS) and p['score'] > 10:
                discoveries.append(f'• {p["title"]} | https://reddit.com{p["permalink"]} | Add as Task in EvyOS: "Explore {p["title"][:50]} (link in notes)"')
    return '\n'.join(discoveries[:8]) or 'No new gems this hour.'

body = f'''🚀 Hourly AI Tools Digest for EvyOS

Paste these directly into your EvyOS Project "AI Tools Radar" as Tasks or Skills:

{mine()}

CSV line example (copy one row):
"New Tool", "reddit-link", "Add as Skill"

Your EvyOS is now auto-fed! Reply "pause" to stop.''' 

# Email (add your Gmail SMTP creds in GitHub secrets or env)
print(body)  # For GH Action
# smtplib code commented – add secrets to enable real email send
print('📧 Digest ready for direct EvyOS paste!')