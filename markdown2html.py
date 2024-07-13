#!/usr/bin/python3

import sys
import os.path
"""Making a file that converts markdown to html
    """

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    elif not os.path.isfile(sys.argv[1]):
        print("Missing {}".format(sys.argv[1]))
        exit(1)

    else:
        exit(0)
