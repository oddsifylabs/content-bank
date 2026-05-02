# Content Bank Workflow Guide

## 🎯 Overview

This system finds sports betting questions across platforms, matches them to pre-written answers, and sends drafts to Jesse for approval before posting.

---

## 📁 Repository Structure

```
content-bank/
├── quora/              # Long-form answers (300-800 words)
├── reddit/             # Medium-form (150-400 words)
├── facebook/           # Short-form + visual (50-150 words)
├── twitter/            # Threads/replies (280 chars × 3-10)
├── scripts/
│   ├── scan-questions.py    # Daily question scanner
│   ├── draft-answer.py      # Answer drafter
│   └── send-for-approval.py # Telegram notifier
├── daily-questions/    # Daily digests (auto-generated)
├── drafts/             # Pending approval drafts
└── README.md
```

---

## 🔄 Daily Workflow

### 10:00 AM PT — Question Scan (Automated)

**Cron job:** `Daily Question Scan (Quora + Reddit)`

1. Runs `scripts/scan-questions.py`
2. Scans Reddit hot posts for questions
3. Generates digest: `daily-questions/YYYY-MM-DD.md`
4. Sends digest to Jesse on Telegram

**Jesse's action:**
- Review digest
- Reply with questions to answer (e.g., "Answer #1 and #3")
- Or say "DRAFT ALL" for top 5

---

### On-Demand — Answer Drafting (Manual trigger)

**When Jesse approves a question:**

1. Run cron job `Draft Answer for Approval` with the question
2. System finds matching template in content-bank
3. Adapts template to specific question
4. Sends draft to Jesse on Telegram

**Jesse's action:**
- Review draft
- Reply "APPROVE" or edit and send back
- Post to platform (or approve for auto-post)

---

### After Posting — Save to Repo

1. Copy final posted answer
2. Save to `content-bank/[platform]/[topic]-[tags].md`
3. Commit to GitHub:
   ```bash
   cd ~/oddsifylabs/content-bank
   git add .
   git commit -m "Add [topic] answer for [platform]"
   git push origin main
   ```

---

## 🏷️ Tagging System

Files are tagged by topic in the filename:

| Tag | Topic | Example |
|-----|-------|---------|
| `[CLV]` | Closing Line Value | `how-does-clv-work-[CLV].md` |
| `[EV]` | Expected Value / +EV | `how-to-find-ev-bets-[EV].md` |
| `[BR]` | Bankroll Management | `good-bankroll-sports-betting-[BR].md` |
| `[LS]` | Line Shopping | `how-many-sportsbooks-[LS].md` |
| `[PSY]` | Psychology / Variance | `handling-losing-streaks-[PSY].md` |
| `[MISC]` | General / Other | `is-betting-rigged-[MISC].md` |

---

## 📋 Platform Guidelines

### Quora (Long-form)
- **Length:** 300-800 words
- **Tone:** Authoritative, detailed
- **Include:** Examples with numbers, GitHub link, Testudo CTA
- **Example:** `quora/how-does-clv-work-[CLV].md`

### Reddit (Medium-form)
- **Length:** 150-400 words
- **Tone:** Conversational, helpful
- **Include:** One key insight, engage with follow-ups
- **Example:** `reddit/parlays-vs-singles-[EV][BR].md`

### Facebook (Short-form)
- **Length:** 50-150 words + visual
- **Tone:** Casual, shareable
- **Include:** One takeaway, graphic/chart
- **Example:** `facebook/realistic-roi-[EV].md`

### Twitter (Thread/Reply)
- **Length:** 280 chars × 3-10 tweets
- **Tone:** Punchy, data-driven
- **Include:** Hook in tweet 1, visual in 2-3, CTA in final
- **Example:** `twitter/bet-sizing-[BR].md`

---

## 🤖 Automation Commands

### Manual Question Scan
```bash
cd ~/oddsifylabs/content-bank
python scripts/scan-questions.py
```

### Manual Answer Draft
```bash
cd ~/oddsifylabs/content-bank
python scripts/draft-answer.py --question "How does CLV work?" --platform quora
```

### Send for Approval
```bash
cd ~/oddsifylabs/content-bank
python scripts/send-for-approval.py drafts/quora-clv-question-20260502.md
```

---

## 📊 Metrics to Track

Weekly review (add to Monday growth report):

| Metric | Target |
|--------|--------|
| Answers posted per week | 5-10 |
| Upvotes/engagement per answer | 20+ (Reddit), 10+ (Quora) |
| Profile follows from answers | 10-20/week |
| Click-throughs to GitHub | Track via bit.ly or similar |

---

## 🎯 Common Question Categories

Use these to match questions to templates:

### Bankroll Management `[BR]`
- How much should I bet per game?
- What's a good starting bankroll?
- How do I avoid going broke?

### CLV / EV `[CLV]` `[EV]`
- What is closing line value?
- How do I find +EV bets?
- Why do sharp bettors care about CLV?

### Line Shopping `[LS]`
- Do I need multiple sportsbooks?
- How much does line shopping matter?
- Which books have the best lines?

### Psychology `[PSY]`
- How do I handle losing streaks?
- Should I chase losses?
- How long until I'm profitable?

### General `[MISC]`
- Is sports betting rigged?
- What's the Turtle Trading system?
- Can you make a living betting?

---

## 🚀 Quick Start (First Time)

1. **Review existing templates:**
   ```bash
   cd ~/oddsifylabs/content-bank
   ls quora/ reddit/ twitter/ facebook/
   ```

2. **Test the scanner:**
   ```bash
   python scripts/scan-questions.py
   ```

3. **Test drafting an answer:**
   ```bash
   python scripts/draft-answer.py --question "What is CLV?" --platform twitter
   ```

4. **Check the draft:**
   ```bash
   cat drafts/twitter-clv-*.md
   ```

---

**Content Bank:** github.com/oddsifylabs/content-bank  
**Testudo Legion:** t.me/testudolegio  
**Track Record:** github.com/oddsifylabs/picks

*Process > Results. CLV > Wins. Patience beats speed.*
