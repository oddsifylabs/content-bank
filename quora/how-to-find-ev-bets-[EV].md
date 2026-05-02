# How do I find +EV bets in sports betting? [EV]

**Answer:**

Finding +EV (positive expected value) bets is the core skill of sharp betting. Here's the complete framework:

## What is +EV?

**Expected Value** = (Win Probability × Profit) - (Loss Probability × Stake)

A bet is +EV when your estimated win probability is **higher** than the implied probability of the odds.

**Example:**
- Odds: -110 (implied 52.4% win rate needed to break even)
- Your model/handicap: 57% win probability
- **Edge: 4.6%** → This is +EV

## Three Ways to Find +EV

### 1. **Market Inefficiencies (Line Shopping)**

Different books have different lines. The gap is your edge.

**Example:**
- DraftKings: Lakers -3.5 (-110)
- FanDuel: Lakers -2.5 (-110)
- **Bet FanDuel** — you get a full point better

Over 500 bets, line shopping adds 3-5% ROI vs. using one book.

### 2. **Statistical Models**

Build or use a model that projects outcomes better than the market.

**Simple approach:**
- Historical data (team stats, player splits, matchups)
- Adjust for context (injuries, rest, weather, umpires)
- Compare your projection to implied odds

**Advanced approach:**
- Machine learning models (we use scanner bots)
- Real-time line monitoring
- Automated alerts when edge ≥4%

### 3. **Information Advantages**

Sometimes you know something the market doesn't (yet).

**Examples:**
- Injury news before it's priced in
- Weather changes (wind in MLB, dome status in NFL)
- Lineup changes (pitcher scratches, NBA load management)

**Warning:** This edge is shrinking. Books adjust faster than ever.

## The 4% Threshold Rule

Not all +EV bets are worth making. We use a **≥4% edge threshold**:

| Your Edge | Verdict |
|-----------|---------|
| 1-2% | Skip (not enough to cover variance) |
| 3-4% | Consider (if confident in model) |
| 4%+ | Bet (meets Testudo Legion standard) |

Why 4%?
- Covers book vig (typically 4.5-5%)
- Accounts for model error
- Survives variance over time

## Tools We Use

**Free:**
- Action Network (line tracking, public % data)
- Covers (line history, closing lines)
- Sportsbook apps (3+ for line shopping)

**Paid/Built:**
- Custom scanner bots (our AlexBET Terminal)
- Pinnacle/Bookmaker EUR (sharper lines for comparison)
- Data feeds (StatsPerform, Sportradar)

## Real +EV Example

**Situation:** NBA player prop
- FanDuel: Jokic Over 24.5 PRA at -115 (implied 53.5%)
- Our model: 58.2% (based on pace, matchup, usage)
- **Edge: 4.7%** → BET

**Why the edge?**
- Opponent (Blazers) = 28th in defensive rating
- Jokic usage: 31.2% with Murray OUT
- Pace: Blazers = 5th fastest last 10 games

We posted this as Pick #038. Result: Jokic had 27 PRA ✅

## Common Mistakes

❌ **Betting your favorite team** (bias destroys EV)  
❌ **Chasing losses** (emotional sizing = -EV)  
❌ **Ignoring the vig** (-110 needs 52.4%, not 50%)  
❌ **Small sample size** (10 bets tells you nothing)  
❌ **No line shopping** (leaving 3-5% ROI on table)

## The Testudo Legion Standard

Our process:
1. Scanner flags edge ≥4%
2. Verify with manual analysis
3. Shop 3+ books for best price
4. Bet 1% bankroll (1u)
5. Track result + CLV

Full audit trail: github.com/oddsifylabs/picks

**Month 1-6 record:** +47 units on 142 bets (33.1% ROI, 56.3% win rate)

---

**Bottom line:** +EV betting is a numbers game. Build a process, track everything, and let math beat luck over time.

*Process > Results. CLV > Wins. Patience beats speed.*
