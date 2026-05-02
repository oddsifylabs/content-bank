#!/usr/bin/env python3
"""
Send draft answer to Telegram for approval.

Called by draft-answer.py to notify Jesse Collins.
"""

import sys
from pathlib import Path

def send_draft_to_telegram(draft_path: str):
    """
    Send draft content to Telegram (Jesse Collins).
    
    Uses the send_message tool via terminal call to hermes.
    """
    draft_file = Path(draft_path)
    
    if not draft_file.exists():
        print(f"ERROR: Draft file not found: {draft_file}")
        return False
    
    with open(draft_file, "r") as f:
        content = f.read()
    
    # Truncate if too long (Telegram limit ~4096 chars)
    if len(content) > 3500:
        content = content[:3500] + "\n\n... (see full draft in repo)"
    
    message = f"""📝 **NEW ANSWER DRAFT FOR APPROVAL**

**Draft File:** `{draft_file.name}`
**Platform:** {draft_file.stem.split('-')[0] if '-' in draft_file.stem else 'Unknown'}

---

{content}

---

**Reply APPROVE to post, or edit and send back.**

**Content Bank:** github.com/oddsifylabs/content-bank
"""
    
    # Output message for cron job to capture and send
    print(message)
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: send-for-approval.py <draft_path>")
        sys.exit(1)
    
    send_draft_to_telegram(sys.argv[1])
