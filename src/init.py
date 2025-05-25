import os
import json

def init_repo():
    """Creates the hidden .miniVCS directory and necessary files."""
    if not os.path.exists(".miniVCS"):
        os.makedirs(".miniVCS")
        
        # Create empty commits file if it doesn't exist
        with open(".miniVCS/commits.json", 'w') as f:
            json.dump([], f)  # Initialize as empty JSON list

        with open(".miniVCS/index.txt", 'w') as f:
            f.write("")  # Empty tracking file

        print("Repository initialized successfully.")
    else:
        print("Repository already exists.")
