import subprocess
import sys

def check_packages():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'list'])
        print("Packages listed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error listing packages: {e}")

if __name__ == "__main__":
    check_packages()