import sys
import re

for line in sys.stdin:
    line = line.strip()
    print(re.sub("human", "computer", line))

