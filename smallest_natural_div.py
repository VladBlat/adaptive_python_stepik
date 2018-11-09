def snd(x, d=2):
    return d if x % d == 0 else snd(x, d+1)
x = int(input())

print(snd(x))