import sys

n = int(sys.stdin.readline())
p2 = list(map(int, sys.stdin.readline().split(' ')))
p1 = list(map(int, sys.stdin.readline().split(' ')))
max = 0
maxi = 0
path = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

for x in range(2, n):
    p0 = list(map(int, sys.stdin.readline().split(' ')))
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

print(path - max)
