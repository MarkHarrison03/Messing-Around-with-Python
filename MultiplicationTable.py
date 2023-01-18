table = [[' '] * 11 for i in range(11)]
for x in range(1, 11):
    for y in range(1, 11):
        table[x][0] = x
        table[0][y] = y
        table[x][y] = x * y

for row in table:
    for x in row:
        print(str(x), end=" ")
    print('\n')

