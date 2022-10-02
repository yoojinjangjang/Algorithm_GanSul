'''
DFs/BFS 실전 문제 4. 미로 탈출
N x M 크기의 미로가 있다. 괴물이 있는 곳은 0, 괴물이 없는 곳은 1로 표시되어 있다.
미로의 출구는 (N, M)의 위치에 존재한다.
동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.

Ex)
5 6
101010
111111
000001
111111
111111

result = 10
'''
from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
maze = deque
for i in range(n):
    maze.append(deque(map(int, input())))



