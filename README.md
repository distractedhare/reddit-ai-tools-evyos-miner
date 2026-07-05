# Reddit + HN + X AI Tools Miner for EvyOS

**Ultra-minimal hourly automation** that watches Reddit, Hacker News, and X for new AI tools, libraries, agents, frameworks & resources — then gives you a **copy-paste block** ready for direct drop into your EvyOS project.

**Zero manual imports or CSVs needed** — just paste the block into EvyOS as Tasks or a Note. Perfect for your "AI Tools Radar" project.

## Quick Start (2-3 mins)
1. Fork or use this repo
2. Go to Settings > Secrets and variables > Actions and add:
   - `X_BEARER_TOKEN` (free! Create at https://developer.x.com → Apps → create Project/App → copy Bearer Token. Basic recent search is free tier.)
   - (Optional) Gmail SMTP if you want auto-email instead of checking Actions log
3. Enable the workflow (Actions tab → enable)
4. In EvyOS: Create Project "AI Tools Radar" or a dedicated Note. Every hour, open the latest Actions run → copy the big "EvyOS AI Tools Radar - Hourly Digest" block → paste straight in.

## How it works
- Pulls fresh posts from top AI subs on Reddit (public JSON)
- Scans new HN stories via official Firebase API (no key)
- Searches recent X posts via official API v2 (Bearer Token, free tier)
- Filters for high-signal AI/tool/launch keywords + engagement
- Outputs one clean paste-ready block with links and suggested EvyOS Task text

**Your EvyOS now has a live AI discovery feed with almost zero effort.**

Tweak SUBREDDITS, KEYWORDS, X_QUERY in miner.py to match your interests. Add more sources easily.

Run manually anytime from Actions tab. Let me know if you want email auto-send, Notion append, or Evy integration tweaks.

Built for Branden @SchulzeBranden — keep building EvyOS! 🚀