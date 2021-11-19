#!/usr/bin/python3

import sys
sum = int(0)

if __name__ == "__main__":
    length = len(sys.argv)
    if length > 1:
        for i in range(1, length):
            sum += int(sys.argv[i])

    print("{:d}".format(sum))
