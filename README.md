# Oddsify Labs Content Bank

Q&A content repository for Oddsify Labs — pre-written answers to common sports betting questions across Quora, Reddit, Facebook, and Twitter.

## 📁 Structure

```
content-bank/
├── quora/              # Long-form educational answers
├── reddit/             # Medium-form conversational responses
├── facebook/           # Short-form + visual content
├── twitter/            # Threads and quote-tweet replies
└── README.md           # This file
```

## 🏷️ Tagging System

Each file is tagged in the filename:
- `[CLV]` — Closing Line Value topics
- `[EV]` — Expected Value / +EV betting
- `[BR]` — Bankroll Management
- `[LS]` — Line Shopping
- `[PSY]` — Betting Psychology / Variance
- `[MISC]` — General questions

Example: `quora/how-does-clv-work-[CLV].md`

## 📋 Content Templates

### Quora (Long-form, 300-800 words)
- Authoritative, detailed
- Include examples with numbers
- Link to GitHub track record
- End with Testudo Legion CTA

### Reddit (Medium-form, 150-400 words)
- Conversational, helpful
- Focus on one key insight
- Link to relevant picks/methodology
- Engage with follow-up questions

### Facebook (Short-form, 50-150 words + visual)
- Casual, shareable
- One clear takeaway
- Graphic or chart included
- Group-friendly tone

### Twitter (Thread or reply, 280 chars × 3-10)
- Punchy, data-driven
- Hook in first tweet
- Visual in tweet 2-3
- CTA in final tweet

## 🎯 Common Question Categories

### Bankroll Management
- How much should I bet per game?
- What's a good bankroll for sports betting?
- How do I avoid going broke?

### CLV / EV
- What is closing line value?
- How do I find +EV bets?
- Why do sharp bettors care about CLV?

### Line Shopping
- Do I really need multiple sportsbooks?
- How much does line shopping matter?
- Which books have the best lines?

### Psychology
- How do I handle losing streaks?
- Should I chase losses?
- How long until I see results?

### Methodology
- What's the Turtle Trading system?
- How many bets until I'm profitable?
- What's a realistic ROI?

## 🔄 Workflow

1. **Daily Question Scan** (10am PT cron)
   - Scrape Quora, Reddit, Twitter for new questions
   - Output: `daily-questions/YYYY-MM-DD.md`

2. **Match to Existing Content**
   - If answer exists → adapt for platform
   - If no match → draft new answer

3. **Telegram Approval**
   - Send draft to Jesse for review
   - Edit if needed

4. **Post + Save**
   - Post to platform
   - Save final version to repo with tags

## 🤖 Automation

```bash
# Run daily question scan
python scripts/scan-questions.py

# Generate answer draft
python scripts/generate-answer.py --question "How does CLV work?"

# Send to Telegram for approval
python scripts/send-for-approval.py --draft drafts/today.md
```

## 📊 Metrics

Track per platform:
- Answers posted per week
- Upvotes/engagement per answer
- Profile follows from answers
- Click-throughs to GitHub/Twitter

---

**Powered by Testudo Legion** — CLV > Wins, Process > Results
