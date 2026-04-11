#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    # Iterate through sys.argv starting from index 1 to skip the script name
    for arg in sys.argv[1:]:
        total += int(arg)
    print("{}".format(total))
