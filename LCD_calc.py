test = {
    '0': [
        " -- ",
        "|  |",
        "|  |",
        "    ",
        "|  |",
        "|  |",
        " -- "
    ],
    '1': [
        "    ",
        "   |",
        "   |",
        "    ",
        "   |",
        "   |",
        "    "
    ],
    '2': [
        " -- ",
        "   |",
        "   |",
        " -- ",
        "|   ",
        "|   ",
        " -- "
    ],
    '3': [
        " -- ",
        "   |",
        "   |",
        " -- ",
        "   |",
        "   |",
        " -- "
    ],
    '4': [
        "    ",
        "|  |",
        "|  |",
        " -- ",
        "   |",
        "   |",
        "    "
    ],
    '5': [
        " -- ",
        "|   ",
        "|   ",
        " -- ",
        "   |",
        "   |",
        " -- ",
    ],
    '6': [
        " -- ",
        "|   ",
        "|   ",
        " -- ",
        "|  |",
        "|  |",
        " -- ",
    ],
    '7': [
        " -- ",
        "   |",
        "   |",
        "    ",
        "   |",
        "   |",
        "    "
    ],
    '8': [
        " -- ",
        "|  |",
        "|  |",
        " -- ",
        "|  |",
        "|  |",
        " -- ",
    ],
    '9': [
        " -- ",
        "|  |",
        "|  |",
        " -- ",
        "   |",
        "   |",
        " -- ",
    ],
}

numbers = list(input())

horizont = 'x' + '-' * (5 * len(numbers) - 1) + 'x'
print(horizont)

for i in range(7):
    for j in range(len(numbers)):
        if j == 0:
            print('|' + test[numbers[j]][i], end=' ')
        elif j == len(numbers) - 1:
            print(test[numbers[j]][i] + '|', end=' ')
        else:
            print(test[numbers[j]][i], end=' ')
    print()

print(horizont)