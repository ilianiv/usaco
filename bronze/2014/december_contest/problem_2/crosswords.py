f = open('crosswords.in', 'r')

[n, m] = list(map(int, f.readline().split(' ')))
field = [row.strip() for row in f]

f.close()

clues = list()

for i in range(n):
    for j in range(m):
        if field[i][j] == '.':
            if (i == 0 or field[i - 1][j] == '#') and i < n - 2 and field[i + 1][j] == '.' and field[i + 2][j] == '.':
                clues.append([i + 1, j + 1])
            elif (j == 0 or field[i][j - 1] == '#') and j < m - 2 and field[i][j + 1] == '.' and field[i][j + 2] == '.':
                clues.append([i + 1, j + 1])

count = len(clues)

f = open('crosswords.out', 'w')
f.write("{0}\n".format(count))

for i in range(count):
    f.write("{0} {1}\n".format(clues[i][0], clues[i][1]))
f.close()
