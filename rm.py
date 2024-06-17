import os
import sys

def rm(paths, recursive):
    for path in paths:
        try:
            if os.path.isfile(path):
                os.remove(path)
                print(f"Successfully removed file '{path}'")
            elif os.path.isdir(path):
                if recursive:
                    os.rmdir(path)
                    print(f"Successfully removed directory '{path}'")
                else:
                    print(f"'{path}' is a directory.")
            else:
                print(f"Error: '{path}' is not a valid file or directory")
        except FileNotFoundError:
            print(f"Error: '{path}' not found.")
        except OSError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    arguments = sys.argv
    if '-r' in arguments:
        recursive = True
        arguments.remove('-r')
    else:
        recursive = False
    paths = arguments[1:]

    rm(paths, recursive)
