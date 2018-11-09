from collections import OrderedDict

n = int(input())

sl_dict = dict()

for i in range(n):
    line = input().split(" - ")
    key = line[0]
    value = line[-1].split(', ')
    sl_dict[key] = value

res = dict()
alph = []

for values in sl_dict.values():
    for value in values:
        alph.append(value)

alph = sorted(alph)

res = OrderedDict()

for key in alph:
    res[key] = []

for key, values in sl_dict.items():
    for res_key in res.keys():
        if res_key in values:
            res[res_key].append(key)

print(len(res))
for key, values in res.items():
    print(key, ' - ', ', '.join(sorted(values)))
