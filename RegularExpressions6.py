import sys
import re

for line in sys.stdin:
    line = line.strip()
    print(re.sub(r"\b[aA]+\b", "argh", line, 1))
