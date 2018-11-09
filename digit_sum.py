def summ(x):
    while True:
        a = x % 10
        yield a
        x = x // 10
        if x:
            continue
        else:
            break

print(sum(summ(int(input()))))

