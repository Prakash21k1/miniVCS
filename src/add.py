import hashlib

def hash_file(file_path):
    """Returns SHA-256 hash of a file."""
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def add_file(file_path):
    """Tracks a file for version control."""
    hash_val = hash_file(file_path)
    with open(".miniVCS/index.txt", "a") as index:
        index.write(f"{file_path}:{hash_val}\n")
    print(f"File '{file_path}' added.")