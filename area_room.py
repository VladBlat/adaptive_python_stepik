cmd = input()

if cmd == "circle":
    r = int(input())
    print(3.14 * (r ** 2))
elif cmd == "rectangle":
    a = int(input())
    b = int(input())
    print(a * b)
elif cmd == "triangle":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    from math import sqrt

    print(sqrt(p * (p - a) * (p - b) * (p - c)))