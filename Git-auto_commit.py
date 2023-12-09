#!/usr/bin/python3
import subprocess

def git_auto_push(commit_message):
    try:
        # Add all changes
        subprocess.run(['git', 'add', '.'])

        # Commit changes
        subprocess.run(['git', 'commit', '-m', commit_message])

        # Push to the remote repository
        subprocess.run(['git', 'push'])

        print("Code added, committed, and pushed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage:
    commit_message = input("Enter commit message: ")
    git_auto_push(commit_message)
