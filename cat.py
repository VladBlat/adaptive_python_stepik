import sys
import re

pattern = re.compile(r"((\W)+|^)cat((\W)+|&)")

for line in sys.stdin:
    test = re.search(pattern, line)
    if test:
        print(line, end='')
    else:
        continue