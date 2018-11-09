from math import ceil

H, A, B = int(input()), int(input()), int(input())

v = A - B
days = 0

while True:
    if H - A <= 0:
        days += 1
        break
    else:
        days += 1
        H = H - v

print(days)


