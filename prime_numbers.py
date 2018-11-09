import numpy as np

def eratosthenes(n):     # n - число, до которого хотим найти простые числа
    sieve = list(range(n + 1))
    sieve[1] = 0    # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve

def bin_search(arr, x):
    lower_bound = 0
    upper_bound = int(arr.shape[0])
    while lower_bound != upper_bound:
        compared_value = (lower_bound + upper_bound) // 2    # Целочисленный тип в Python имеет неограниченную длину
        if x == arr[compared_value]:
            return compared_value
        elif x < arr[compared_value]:
            upper_bound = compared_value
        else:
            lower_bound = compared_value + 1
    return None  # если цикл окончен, то значение не найденно

n = int(input())
idxs = list(map(int, input().split()))

primes = np.array(eratosthenes(3000000))
primes = primes[primes != 0]

all_idxs = np.array(list(range(1, len(primes) + 1)))

for idx in idxs:
    print(primes[bin_search(all_idxs, idx)], end=' ')