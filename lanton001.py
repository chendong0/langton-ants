import os
import random
import time

periods = 11000
m = 60
n = 102
cells = [[0] * n for i in range(m)]

# 0 -x, 1 +y, 2 +x, 3 -y
direct = random.randint(0, 3)
cells = [[0] * n for i in range(m)]
i = random.randint(0, m - 1)
j = random.randint(0, n - 1)
cells[i][j] = 1

for k in range(periods):
        os.system('clear')
        print("Step %d" % (k + 1))
        if cells[i][j] == 1:
                direct = (direct - 1) % 4
                cells[i][j] = 0
        else:
                direct = (direct + 1) % 4
                cells[i][j] = 1
        if direct == 0:
                j = (j - 1) % n
        elif direct == 1:
                i = (i - 1) % m
        elif direct == 2:
                j = (j + 1) % n
        else:
                i = (i + 1) % m
        for x in range(m):
                for y in range(n):
                        if cells[x][y] == 1:
                                print('*', end=' ')
                        else:
                                print(' ', end=' ')
                print()
        time.sleep(0.05)
