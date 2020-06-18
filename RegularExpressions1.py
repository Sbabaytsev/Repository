import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r"cat"
    match = re.findall(pattern, line)
    print(match)
    if len(match) > 1:
        print(line)
