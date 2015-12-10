import sys

[n, m] = list(map(int, sys.stdin.readline().split(' ')))
field = [row.strip() for row in sys.stdin]
clues = list()

for i in range(n):
    for j in range(m):
        if field[i][j] == '.':
            if (i == 0 or field[i - 1][j] == '#') and i < n - 2 and field[i + 1][j] == '.' and field[i + 2][j] == '.':
                clues.append([i + 1, j + 1])
            elif (j == 0 or field[i][j - 1] == '#') and j < m - 2 and field[i][j + 1] == '.' and field[i][j + 2] == '.':
                clues.append([i + 1, j + 1])

count = len(clues)
print(count)

for i in range(count):
    print("{0} {1}".format(clues[i][0], clues[i][1]))
