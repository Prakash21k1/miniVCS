import json
def checkout(commit_index):
    """Restores files from a specific commit."""
    with open(".miniVCS/commits.json", "r") as commit_file:
        commits = json.load(commit_file)

    if commit_index >= len(commits):
        print("Invalid commit index.")
        return

    commit = commits[commit_index]
    print(f"Restoring commit: {commit['message']}")
    for file in commit['files']:
        print(f"  - Restoring {file['file']} (hash: {file['hash']})")

checkout(0)  # Restore the first commit