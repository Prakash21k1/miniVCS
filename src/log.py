import json
import os

def log_commits():
    """Displays commit history."""
    if not os.path.exists(".miniVCS/commits.json"):
        print("No commits found.")
        return

    with open(".miniVCS/commits.json", "r") as commit_file:
        commits = json.load(commit_file)

    for commit in commits:
        print(f"Commit: {commit['message']}, Timestamp: {commit['timestamp']}")
        for file in commit['files']:
            print(f"  - {file['file']} ({file['hash']})")