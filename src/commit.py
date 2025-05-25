import json
import time
import os

def commit(message):
    """Commits tracked file changes with a message."""
    commit_data = {
        "message": message,
        "timestamp": time.time(),
        "files": []
    }

    with open(".miniVCS/index.txt", "r") as index:
        for line in index.readlines():
            file_path, hash_val = line.strip().split(":")
            commit_data["files"].append({"file": file_path, "hash": hash_val})

    commits = []
    if os.path.exists(".miniVCS/commits.json"):
        with open(".miniVCS/commits.json", "r") as commit_file:
            try:
                commits = json.load(commit_file)
            except json.JSONDecodeError:
                commits = []

    commits.append(commit_data)

    with open(".miniVCS/commits.json", "w") as commit_file:
        json.dump(commits, commit_file, indent=4)

    print(f"Commit successful: {message}")