f = open('marathon.in', 'r')

n = int(f.readline())
p2 = list(map(int, f.readline().split(' ')))
p1 = list(map(int, f.readline().split(' ')))
max = 0
maxi = 0
path = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

for x in range(2, n):
    p0 = list(map(int, f.readline().split(' ')))
    diff21 = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
    diff01 = abs(p0[0] - p1[0]) + abs(p0[1] - p1[1])
    diff02 = abs(p0[0] - p2[0]) + abs(p0[1] - p2[1])
    tmp = diff21 + diff01 - diff02
    if max < tmp:
        max = tmp
        maxi = x - 1
    p2 = p1
    p1 = p0
    path += diff01

f.close()

f = open('marathon.out', 'w')
f.write("{0}\n".format(path - max))
f.close()

