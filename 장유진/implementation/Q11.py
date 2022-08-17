'''
Q11. 뱀
https://velog.io/@yoojinjangjang/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-3190
: 장유진 벨로그 놀러오셈~:)
'''

import sys

input = sys.stdin.readline

N = int(input())
n = [[0]*N for _ in range(N)]

k = int(input())
for i in range(k):
    x,y = map(int,input().split())
    n[x-1][y-1] = 1

#sx,sy 좌표 변화값 리스트
l = [(0,1),(1,0),(0,-1),(-1,0)]
d = 0
#초기값 설정
x = 0
y = 0
sx = 0
sy = 1
cnt = 1
snake_list = [(0,0)]
i = 0
L = int(input())
rotate = []
for _ in range(L):
    a,b = input().split()
    rotate.append([a,b])

# 반복문 시작
while True:
    x += sx
    y += sy
    if (x,y) in snake_list or x >= N or x<0 or y >= N or y < 0:
        break
    if n[x][y] == 1:
        snake_list.append((x,y))
        n[x][y] = 0
    else:
        snake_list.pop(0)
        snake_list.append((x,y))
    if i < len(rotate) and cnt == int(rotate[i][0]) :
        if rotate[i][1] == 'L':
            d = (d-1)%4
        else:
            d = (d+1)%4
        sx,sy = l[d]
        i += 1
    cnt += 1
print(cnt)