import sys

if __name__ == "__main__":
    for i in sys.argv:
        with open(i, '+a') as file:
            pass
