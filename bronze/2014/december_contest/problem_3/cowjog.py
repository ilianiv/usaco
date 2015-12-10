f = open('cowjog.in', 'r')

n = int(f.readline())
row = [0]

for i in range(n):
    [pos, speed] = list(map(int, f.readline().split(' ')))

    back = -1

    while len(row) + back > 0 and row[back] > speed:
        row.pop()

    row.append(speed)

f.close()

f = open('cowjog.out', 'w')
f.write("{0}\n".format(len(row) - 1))
f.close()
