import numpy as np

test = np.ndarray(shape=(3, 4), dtype=int, order='F')

for i in range(3):
    for j in range(4):
        if i == j:
            test[i, j] = 2
        elif j == i + 1:
            test[i, j] = 1
        else:
            test[i, j] = 0


# to eye
# test.


print(test)