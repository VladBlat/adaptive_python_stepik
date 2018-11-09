def trans(in_number, num_dict):
    from collections import OrderedDict

    test = 'I' * in_number
    num_dict = OrderedDict(sorted(num_dict.items(), key=lambda t: t[1], reverse=True))

    for key, value in num_dict.items():
        test = test.replace('I' * value, key)

    # # zamena
    # test = test.replace('VIIII', "IX")
    # test = test.replace('LXXXX', "XC")
    # test = test.replace('DCCCC', "CM")
    #
    # test = test.replace('I' * 4, "IV")
    # test = test.replace('X' * 4, "XL")
    # test = test.replace('C' * 4, "MC")

    return test

romanian_numbers = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

while True:
    print(trans(int(input()), romanian_numbers))