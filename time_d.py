time1 = []
for i in range(3):
    time1.append(int(input()))

time2 = []
for j in range(3):
    time2.append(int(input()))

h = (time2[0] - time1[0]) * 3600
m = (time2[1] - time1[1]) * 60
s = time2[2] - time1[2]

print(h + m + s)