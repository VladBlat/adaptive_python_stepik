import sys

res = dict()

for line in sys.stdin:
    tmp = line.split()

    if res.get(tmp[0]):
        res[tmp[0]].append(int(tmp[-1]))
    else:
        res[tmp[0]] = []
        res[tmp[0]].append(int(tmp[-1]))

for key in res.keys():
    avg = sum(res[key])/len(res[key])
    res[key] = avg
    print(key, res[key], sep='\t')




