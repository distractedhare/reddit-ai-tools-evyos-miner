# Reddit AI Tools & Resources Miner for EvyOS

🚀 **Fully working automation** that mines Reddit hourly for new AI tools, libraries, apps, papers & resources.

**Runs every hour** via GitHub Actions ✅
**Feeds discoveries** to Notion DB (easy copy/import to EvyOS) + CSV export for direct EvyOS import + Markdown summaries.

## Quick Start
1. ⭐ Star this repo
2. Add secrets in Settings > Secrets and variables > Actions:
   - `REDDIT_USER_AGENT` (optional)
   - `NOTION_TOKEN` (your integration token)
   - `NOTION_DATABASE_ID` (from your 🧠 AI Reddit Discoveries DB)
   - Optional: `OPENAI_API_KEY` or Grok key for smarter summaries
3. Enable workflow in Actions tab
4. In EvyOS: Create Project "AI Tools Radar" → Import CSV or paste from Notion/Drive

## How it works
- Polls 12+ top AI subreddits + Reddit search for "AI tool" etc.
- Filters high-signal posts (upvotes, keywords, no spam)
- Extracts structured data with simple logic (extendable with LLM)
- Appends to Notion + commits CSV/MD

Clone & customize in 2 mins! Fork recommended.

**Your EvyOS is now auto-fed with fresh AI gold every hour 🔥**