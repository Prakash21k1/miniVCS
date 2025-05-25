import argparse
from src.init import init_repo
from src.add import add_file
from src.commit import commit
from src.log import log_commits
from src.checkout import checkout

parser = argparse.ArgumentParser(description="Mini Version Control System CLI")
parser.add_argument("command", help="Command to execute (init, add, commit, log, checkout)")
parser.add_argument("arg", nargs="?", help="Additional argument (file or message)")
args = parser.parse_args()

if args.command == "init":
    init_repo()
elif args.command == "add" and args.arg:
    add_file(args.arg)
elif args.command == "commit" and args.arg:
    commit(args.arg)
elif args.command == "log":
    log_commits()
elif args.command == "checkout" and args.arg.isdigit():
    checkout(int(args.arg))
else:
    print("Invalid command. Use: init, add <file>, commit <message>, log, checkout <index>")