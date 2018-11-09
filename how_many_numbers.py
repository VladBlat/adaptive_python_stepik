N = input()
arr = list(map(int, input().split()))
requests_count = int(input())
requests = []
for i in range(requests_count):
    tmp = tuple(map(int, input().split()))
    requests.append(range(tmp[0], tmp[1]))

# print(requests)
res = [0, 0, 0]

for idx, request in enumerate(requests):
    for number in arr:
        if number in request:
            res[idx] += 1

print(*res)