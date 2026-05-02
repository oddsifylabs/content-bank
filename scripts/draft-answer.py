#!/usr/bin/env python3
"""
Answer Drafter for Oddsify Labs Content Bank

Matches questions to existing templates, drafts platform-specific answers,
and sends to Telegram for approval.

Usage: python draft-answer.py --question "QUESTION TEXT" --platform [quora|reddit|twitter|facebook]
"""

import argparse
import json
from datetime import datetime
from pathlib import Path
import subprocess

# Content bank paths
CONTENT_BANK = Path.home() / "oddsifylabs" / "content-bank"
DRAFTS_DIR = CONTENT_BANK / "drafts"
DRAFTS_DIR.mkdir(parents=True, exist_ok=True)

def find_matching_template(question: str, platform: str) -> Path | None:
    """
    Find existing template that matches the question.
    
    Simple keyword matching - in production, use embeddings/semantic search.
    """
    question_lower = question.lower()
    
    # Keyword to tag mapping
    keyword_map = {
        "clv": "[CLV]",
        "closing line": "[CLV]",
        "bankroll": "[BR]",
        "stake": "[BR]",
        "bet size": "[BR]",
        "ev": "[EV]",
        "+ev": "[EV]",
        "expected value": "[EV]",
        "line shopping": "[LS]",
        "sportsbooks": "[LS]",
        "books": "[LS]",
        "parlay": "[EV]",
        "losing streak": "[PSY]",
        "variance": "[PSY]",
        "turtle": "[MISC]",
        "profitable": "[PSY]",
        "roi": "[EV]",
        "rigged": "[MISC]",
    }
    
    # Find matching tags
    matched_tags = []
    for keyword, tag in keyword_map.items():
        if keyword in question_lower:
            matched_tags.append(tag)
    
    if not matched_tags:
        return None
    
    # Search for templates with matching tags
    platform_dir = CONTENT_BANK / platform
    if not platform_dir.exists():
        return None
    
    for template in platform_dir.glob("*.md"):
        for tag in matched_tags:
            if tag in template.name:
                return template
    
    # Fallback: search all platforms
    for platform in ["quora", "reddit", "twitter", "facebook"]:
        platform_dir = CONTENT_BANK / platform
        if platform_dir.exists():
            for template in platform_dir.glob("*.md"):
                for tag in matched_tags:
                    if tag in template.name:
                        return template
    
    return None

def load_template(template_path: Path) -> str:
    """Load template content."""
    with open(template_path, "r") as f:
        return f.read()

def adapt_template(template: str, platform: str, question: str) -> str:
    """
    Adapt template to platform and specific question.
    
    In production, this would use an LLM to customize the response.
    For now, adds question context and platform formatting.
    """
    # Add question header
    adapted = f"""# Answer Draft | {datetime.now().strftime("%Y-%m-%d %H:%M")}

**Question:** {question}

**Platform:** {platform}

**Source Template:** {template_path.name if (template_path := find_matching_template(question, platform)) else "Custom draft"}

---

"""
    adapted += template
    
    # Add footer for approval workflow
    adapted += f"""

---

**Approval Status:** ⏳ Pending Jesse review

**To approve:** Reply "APPROVE" or edit and send back

**To post manually:** Copy answer above, post to {platform}, then save final version to content-bank/{platform}/
"""
    
    return adapted

def send_to_telegram(draft_path: Path):
    """Send draft to Telegram for approval."""
    
    # Read the draft
    with open(draft_path, "r") as f:
        draft_content = f.read()
    
    # Format message
    message = f"""📝 **NEW ANSWER DRAFT FOR APPROVAL**

**Question:** See draft file
**Platform:** {draft_path.stem.split('-')[0] if '-' in draft_path.stem else 'Unknown'}
**Draft:** `{draft_path}`

---

{draft_content[:3000]}{'...' if len(draft_content) > 3000 else ''}

---

**Reply APPROVE to post, or edit and send back.**
"""
    
    # Send via send_message tool (would be called by cron job)
    # For now, just print the message
    print(f"\n📤 Would send to Telegram:")
    print(message[:500])
    
    return message

def main():
    parser = argparse.ArgumentParser(description="Draft answer for sports betting question")
    parser.add_argument("--question", type=str, required=True, help="The question to answer")
    parser.add_argument("--platform", type=str, default="quora", 
                       choices=["quora", "reddit", "twitter", "facebook"],
                       help="Target platform")
    parser.add_argument("--custom", action="store_true", help="Force custom draft (no template matching)")
    
    args = parser.parse_args()
    
    print(f"📝 Drafting answer for: {args.question[:50]}...")
    print(f"🎯 Platform: {args.platform}\n")
    
    # Find matching template
    template_path = None
    if not args.custom:
        template_path = find_matching_template(args.question, args.platform)
    
    if template_path:
        print(f"✅ Found matching template: {template_path.name}")
        template = load_template(template_path)
    else:
        print(f"⚠️  No matching template found, creating custom draft...")
        # Determine tone based on platform
        if args.platform == "quora":
            tone = "Authoritative, detailed (Quora)"
        elif args.platform == "reddit":
            tone = "Conversational, helpful (Reddit)"
        elif args.platform == "twitter":
            tone = "Punchy, data-driven (Twitter)"
        else:
            tone = "Casual, shareable (Facebook)"
        
        template = f"""[Custom draft needed for: {args.question}]

**Key points to cover:**
1. [Main concept explanation]
2. [Example with numbers]
3. [Testudo Legion methodology tie-in]
4. [CTA: GitHub track record / Telegram community]

**Tone:** {tone}

---

*Draft this answer based on the question above, then save to content-bank/{args.platform}/*"""
    
    # Adapt for platform
    draft_content = adapt_template(template, args.platform, args.question)
    
    # Save draft
    timestamp = datetime.now().strftime("%Y%m%d-%H%M")
    safe_question = args.question[:30].replace(" ", "-").replace("?", "")
    draft_file = DRAFTS_DIR / f"{args.platform}-{safe_question}-{timestamp}.md"
    
    with open(draft_file, "w") as f:
        f.write(draft_content)
    
    print(f"✅ Draft saved: {draft_file}")
    
    # Send to Telegram
    send_to_telegram(draft_file)
    
    print(f"\n📄 Full draft: {draft_file}")
    return str(draft_file)

if __name__ == "__main__":
    main()
