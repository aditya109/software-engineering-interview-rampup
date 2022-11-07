import os
import os.path
from os import path
import re


def main():
    l = os.getcwd()
    a = [x[0] for x in os.walk(l)]
    count = 1
    for dir in a:
        # if not re.search("git", dir) and dir != "." and not re.search("vscode", dir) and dir != l:
        p = os.path.join(l, os.path.join(dir, "README.md"))
        with open(p, 'w') as fp:
            pass
        if path.isfile(p):
            print("README.md created at " + p + " location")
        else:
            print("README.md creation FAILED at " + p + " location")


main()