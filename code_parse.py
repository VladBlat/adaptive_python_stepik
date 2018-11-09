import re
import sys
import itertools

ident = "([A-Za-z]|\_)(\w|\_)*"
atribute = ident + '(\.' + ident + ')?'
couple = atribute + '(' + '\,\s' + atribute + ')*'
assignation = couple + "\s\="
#
# itog1 = []
# itog2 = []
# itog3 = []
# itog4 = []
#
# with open("code_parse_test_1.txt", "r") as test:
#     idxs = itertools.count(1)
#     for line in test:
#         # print(line, end='')
#         idx = next(idxs)
#         res = re.match(assignation, line.lstrip())
#         if res:
#             tmp = list(res.group())
#             while True:
#                 try:
#                     tmp.remove(',')
#                 except ValueError:
#                     res = ''.join(tmp[0:-2])
#                     break
#             itog1.append((idx, res))
#         else:
#             pass
#
# for i in itog1:
#     print(i[0], i[1])
#
# print()
#
# with open("code_parse_test_2.txt", "r") as test:
#     idxs = itertools.count(1)
#     for line in test:
#         # print(line, end='')
#         idx = next(idxs)
#         res = re.match(assignation, line.lstrip())
#         if res:
#             tmp = list(res.group())
#             while True:
#                 try:
#                     tmp.remove(',')
#                 except ValueError:
#                     res = ''.join(tmp[0:-2])
#                     break
#             itog2.append((idx, res))
#         else:
#             pass
#
# for i in itog2:
#     print(i[0], i[1])
#
# print()
#
# with open("code_parse_test_3.txt", "r") as test:
#     idxs = itertools.count(1)
#     for line in test:
#         # print(line, end='')
#         idx = next(idxs)
#         res = re.match(assignation, line.lstrip())
#         if res:
#             tmp = list(res.group())
#             while True:
#                 try:
#                     tmp.remove(',')
#                 except ValueError:
#                     res = ''.join(tmp[0:-2])
#                     break
#             itog3.append((idx, res))
#         else:
#             pass
#
# for i in itog3:
#     print(i[0], i[1])
#
# print()
#
# with open("code_parse_test_4.txt", "r") as test:
#     idxs = itertools.count(1)
#     for line in test:
#         # print(line, end='')
#         idx = next(idxs)
#         res = re.match(assignation, line.lstrip())
#         if res:
#             tmp = list(res.group())
#             while True:
#                 try:
#                     tmp.remove(',')
#                 except ValueError:
#                     res = ''.join(tmp[0:-2])
#                     break
#             itog4.append((idx, res))
#         else:
#             pass
#
# for i in itog4:
#     print(i[0], i[1])

idxs = itertools.count(1)
for line in sys.stdin:
    # print(line)
    idx = next(idxs)
    res = re.match(assignation, line.lstrip())
    if res:
        # print("in")
        tmp = list(res.group())
        while True:
            try:
                tmp.remove(',')
            except ValueError:
                res = ''.join(tmp[0:-2])
                break
        print(idx, res)
    else:
        pass



