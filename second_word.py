import re
test = re.search(r'\,\s(\w)+', input())
print(test.group()[2:])