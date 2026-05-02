#!/usr/bin/env python3
"""
Daily Question Scanner for Oddsify Labs Content Bank

Scans Quora, Reddit, and Twitter for sports betting questions.
Outputs daily digest for content creation.

Usage: python scan-questions.py [--output PATH]
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Output directory
OUTPUT_DIR = Path.home() / "oddsifylabs" / "content-bank" / "daily-questions"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Search queries for each platform
QUORA_QUERIES = [
    "sports betting closing line value",
    "how to bet sports EV",
    "sports betting bankroll management",
    "line shopping sportsbooks",
    "Turtle Trading betting",
    "how to find +EV bets",
    "sports betting losing streak",
    "parlay vs single bets",
]

REDDIT_QUERIES = [
    "r/sportsbook daily discussion",
    "r/CFBets picks",
    "r/SportsBetting advice",
    "sports betting CLV",
    "EV betting strategy",
]

TWITTER_QUERIES = [
    "sports betting help",
    "how to bet on sports",
    "betting advice",
    "CLV betting",
    "EV picks",
]

def scan_quora():
    """
    Scan Quora for sports betting questions.
    
    Note: Quora doesn't have a public API for free scraping.
    This uses RSS feeds from Quora topic pages.
    
    Alternative: Use web_search tool to find recent questions.
    """
    questions = []
    
    # For now, return placeholder structure
    # In production, this would use:
    # - Quora RSS feeds (topic-based)
    # - web_search tool for recent questions
    # - Manual curation from high-traffic topics
    
    print("📍 Quora scan: Using web_search for questions...")
    
    # Placeholder - will be populated by actual search in cron job
    return questions

def scan_reddit():
    """
    Scan Reddit for sports betting questions.
    
    Uses Reddit's public JSON API (no auth required for read-only).
    """
    questions = []
    
    subreddits = ["sportsbook", "CFBets", "SportsBetting"]
    
    for sub in subreddits:
        try:
            # Get hot posts from subreddit
            url = f"https://www.reddit.com/r/{sub}/hot.json?limit=25"
            import urllib.request
            import ssl
            
            # Bypass SSL verification for simple scraping
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            
            req = urllib.request.Request(url, headers={"User-Agent": "OddsifyLabs/1.0"})
            with urllib.request.urlopen(req, context=ctx) as response:
                data = json.loads(response.read().decode())
            
            for post in data.get("data", {}).get("children", []):
                post_data = post.get("data", {})
                title = post_data.get("title", "")
                
                # Filter for question-like posts
                if any(q in title.lower() for q in ["?", "how", "what", "should i", "advice", "help"]):
                    questions.append({
                        "platform": "reddit",
                        "subreddit": sub,
                        "title": title,
                        "url": f"https://reddit.com{post_data.get('permalink', '')}",
                        "score": post_data.get("score", 0),
                        "comments": post_data.get("num_comments", 0),
                        "created": datetime.fromtimestamp(post_data.get("created_utc", 0)).isoformat(),
                    })
        except Exception as e:
            print(f"  ⚠️  Error scanning r/{sub}: {e}")
    
    return questions

def scan_twitter():
    """
    Scan Twitter for sports betting questions.
    
    Uses xurl CLI if available, otherwise returns placeholder.
    """
    questions = []
    
    # Check if xurl is available
    import subprocess
    try:
        result = subprocess.run(
            ["xurl", "--app", "oddsify-labs", "/2/tweets/search/recent",
             "-q", "sports betting help OR how to bet on sports -filter:retweets"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            for tweet in data.get("data", []):
                questions.append({
                    "platform": "twitter",
                    "text": tweet.get("text", ""),
                    "id": tweet.get("id", ""),
                    "created": tweet.get("created_at", ""),
                })
    except FileNotFoundError:
        print("  ⚠️  xurl not found, skipping Twitter scan")
    except Exception as e:
        print(f"  ⚠️  Twitter scan error: {e}")
    
    return questions

def generate_digest(questions):
    """Generate a markdown digest of all questions."""
    
    today = datetime.now().strftime("%Y-%m-%d")
    output_file = OUTPUT_DIR / f"{today}.md"
    
    # Sort by platform
    by_platform = {"quora": [], "reddit": [], "twitter": []}
    for q in questions:
        platform = q.get("platform", "unknown")
        by_platform[platform].append(q)
    
    content = f"""# Daily Question Digest | {today}

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M")}

---

## 📍 Quora ({len(by_platform['quora'])} questions)

"""
    
    if by_platform["quora"]:
        for q in by_platform["quora"]:
            content += f"""
### {q.get('question', 'Unknown question')}
- **URL:** {q.get('url', 'N/A')}
- **Tags:** {q.get('tags', [])}
- **Suggested template:** [Match to content-bank topic]

"""
    else:
        content += "*No Quora questions scanned (requires manual search or RSS setup)*\n\n"
    
    content += f"""## 📱 Reddit ({len(by_platform['reddit'])} questions)

"""
    
    if by_platform["reddit"]:
        for q in by_platform["reddit"][:10]:  # Top 10
            content += f"""
### {q['title']}
- **Subreddit:** r/{q['subreddit']}
- **Score:** {q['score']} | **Comments:** {q['comments']}
- **URL:** {q['url']}
- **Suggested template:** [Match to content-bank topic]

"""
    else:
        content += "*No Reddit questions found*\n\n"
    
    content += f"""## 🐦 Twitter ({len(by_platform['twitter'])} questions)

"""
    
    if by_platform["twitter"]:
        for q in by_platform["twitter"][:10]:  # Top 10
            content += f"""
### {q['text'][:100]}...
- **Tweet ID:** {q['id']}
- **Posted:** {q['created']}
- **Suggested template:** [Match to content-bank topic]

"""
    else:
        content += "*No Twitter questions scanned (xurl required)*\n\n"
    
    content += f"""---

## 🎯 Action Items

1. Review questions above
2. Match to existing content-bank templates
3. Draft new answers for unmatched questions
4. Send drafts to Telegram for approval
5. Post approved answers + save to repo

---

**Content Bank:** github.com/oddsifylabs/content-bank  
**Approval:** Telegram → Jesse Collins
"""
    
    with open(output_file, "w") as f:
        f.write(content)
    
    print(f"✅ Digest saved to: {output_file}")
    return output_file

def main():
    print("🔍 Starting daily question scan...\n")
    
    all_questions = []
    
    # Scan Quora (placeholder for now)
    print("📍 Scanning Quora...")
    quora_q = scan_quora()
    all_questions.extend(quora_q)
    print(f"   Found {len(quora_q)} questions\n")
    
    # Scan Reddit
    print("📱 Scanning Reddit...")
    reddit_q = scan_reddit()
    all_questions.extend(reddit_q)
    print(f"   Found {len(reddit_q)} questions\n")
    
    # Scan Twitter
    print("🐦 Scanning Twitter...")
    twitter_q = scan_twitter()
    all_questions.extend(twitter_q)
    print(f"   Found {len(twitter_q)} questions\n")
    
    # Generate digest
    print("📝 Generating digest...")
    digest_file = generate_digest(all_questions)
    
    print(f"\n✅ Complete! Total questions: {len(all_questions)}")
    print(f"📄 Digest: {digest_file}")
    
    # Output for cron job to capture
    return str(digest_file)

if __name__ == "__main__":
    main()
