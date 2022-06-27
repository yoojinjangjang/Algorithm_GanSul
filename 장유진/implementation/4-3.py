'''
Q4-3] 왕실의 나이트
: 8*8 좌표 평면, 나이트 -> 수평 두칸 수직 한칸 or 수직 두칸 수평 한칸
: 나이트의 위치가 주어졌을때 나이트가 이동할 수 있는 경우의 수를 출력
: 행의 위치 1~8, 열의 위치 a~h

입력 : 현재 나이트 위치의 좌표
출력 : 경우의 수
'''

import sys

input = sys.stdin.readline

loc = input()
col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row = ['1', '2', '3', '4', '5', '6', '7', '8']

count = 0

pos = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

for i in pos:
    after = (col.index(loc[0]) + i[0], row.index(loc[1]) + i[1])
    if 0 <= after[0] <= 7 and 0 <= after[1] <= 7:
        count += 1
print(count)
