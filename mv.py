import shutil
import os
import sys

def mv(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Successfully moved '{source}' to '{destination}'")
    except FileNotFoundError:
        print(f"Error: '{source}' not found.")
    except FileExistsError:
        print(f"Error: '{destination}' already exists.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python mv.py <source> <destination>")
        sys.exit(1)
    
    source = sys.argv[1]
    destination = sys.argv[2]
    
    mv(source, destination)
