import shutil
import os
import sys

def cp(source, destination):
    try:
        if os.path.isdir(source):
            shutil.copytree(source, destination)
        else:
            shutil.copy2(source, destination)
        print(f"Successfully copied '{source}' to '{destination}'")
    except FileNotFoundError:
        print(f"Error: '{source}' not found.")
    except FileExistsError:
        print(f"Error: '{destination}' already exists.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python cp.py <source> <destination>")
        sys.exit(1)
    
    source = sys.argv[1]
    destination = sys.argv[2]
    
    cp(source, destination)
