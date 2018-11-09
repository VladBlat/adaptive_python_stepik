coming_msg = input()

letters = set(coming_msg)

from collections import OrderedDict

letters_counts = dict()
for letter in letters:
    letters_counts[letter] = coming_msg.count(letter)

letters_counts = OrderedDict(sorted(letters_counts.items(), key=lambda t: t[1]))

codes = OrderedDict()
for key in letters_counts.keys():
    codes[key] = ""

def by_len(x):
    return len(x[0])


tmp = list(letters_counts.items())

if len(tmp) == 1:
    for key in codes.keys():
        codes[key] = '0'
else:
    while len(tmp) > 1:
        new = (tmp[0][0] + tmp[1][0], tmp[0][1] + tmp[1][1])
        for letter in tmp[0][0]:
            codes[letter] = '1' + codes[letter]
        for letter in tmp[1][0]:
            codes[letter] = '0' + codes[letter]
        tmp.append(new)
        tmp.pop(0)
        tmp.pop(0)
        tmp.sort(key=by_len, reverse=True)
        tmp.sort(key=lambda x: x[1])

incoded_string = ""
for letter in coming_msg:
    incoded_string += codes[letter]

print("{} {}".format(len(letters), len(incoded_string)))
codes = OrderedDict(sorted(codes.items(), key=lambda x: x[0]))
for key, value in codes.items():
    print("{}: {}".format(key, value))
print(incoded_string)