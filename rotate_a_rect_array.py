import numpy as np

n, m = tuple(map(int, input().split()))
# n - height, m - width
res = []
for i in range(n):
    raw = list(map(int, input().split()))
    if len(raw) == m:
        res.append(raw)
    else: exit()

tmp = np.array(res)
res = np.fliplr(tmp.T)
for i in range(m):
    for j in range(n):
        print(res[i, j], end=' ')
    print()