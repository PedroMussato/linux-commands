import os
import sys

if __name__ == "__main__":
    path = sys.argv[1]

    os.rmdir(path)
