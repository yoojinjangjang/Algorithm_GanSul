'''
왕실의 나이트
'''

import sys

nite = list(sys.stdin.readline().strip())
row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x, y = nite[0], int(nite[1])
cnt = 0

for i in range(len(row)):
    if nite[0] == row[i]:
        x = i + 1

# 수평으로 두 칸 이동 수직 한 칸
# 수직으로 두 칸 이동 수평 한 칸
dx = [1, -1, 1, -1, -2, -2, 2, 2]
dy = [-2, -2, 2, 2, 1, -1, 1, -1]

for i in range(8):
    x, y = x + dx[i], y + dy[i]
    if 0 < x < 9 and 0 < y < 9:
        cnt += 1

print(cnt)
