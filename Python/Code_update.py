import subprocess

def update_vscode():
    # Run the system command to update VS Code
    command = "sudo apt update && sudo apt upgrade code"
    process = subprocess.Popen(command, shell=True)
    process.wait()

if __name__ == "__main__":
    update_vscode()
    print("VS Code has been updated.")
