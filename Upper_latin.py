res = lambda x: x.swapcase() if ord(x) <= 122 else x

print(res(input()))
