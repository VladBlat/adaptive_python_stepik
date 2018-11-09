import sys
import re

pattern = r"(\d)\1\1"

for line in sys.stdin:
    test = re.search(pattern, line)
    if test:
        print(line, end='')
    else:
        continue