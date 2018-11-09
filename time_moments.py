n = int(input())

times = []

for i in range(n):
    times.append(list(map(int, input().split())))

times.sort()

for time in times:
    print(' '.join(str(x) for x in time))
