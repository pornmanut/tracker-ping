import os
import sys
import re

args = sys.argv
if len(args) <= 1:
    print("need more arugment")
    sys.exit()


target = args[1]
ip4 = []
if os.path.exists(target):
    with open(target) as fo:
        print("reading from "+fo.name)
        for line in fo:
            mask = re.search('(?:[0-9]{1,3}\.){3}[0-9]{1,3}', line)
            if mask:
                ip4.append(line[mask.start(): mask.end()])

print(ip4)
