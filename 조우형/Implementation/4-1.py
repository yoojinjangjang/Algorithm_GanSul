'''
구현 실전 문제 1. 상하좌우
여행가 A가 N x N 크기의 정사각형 공간에서 L, R, U, D 방향으로 한 칸씩 움직인다고 할 때,
여행가 A가 최종적으로 도착해 있는 곳의 좌표를 구하시오.
시작 좌표는 항상 (1, 1) 이다.

Ex) input : 5
R R R U D D

result : 3 4
'''
import sys

n = int(sys.stdin.readline()) # N x N 정사각형 크기
inputs = list(sys.stdin.readline().split()) # 이동 방향

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
d = ['L', 'R', 'U', 'D']

for input in inputs:
    for i in range(len(d)):
        if input == d[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny <1 or nx >n or ny > n:
        continue

    x, y = nx, ny

print(x, y)


