"""
백준 그리디 1931
한 개의 회의실에서 겹치지 않고 회의가 일어날 수 있는 최대 개수를 출력하라.

ex) N = 11 회의 수
K = (출발시간, 종료시간)
출력 : 최대 개수
"""
import sys

N = int(sys.stdin.readline())
K = []

for i in range(N):
    K.append(tuple(map(int, sys.stdin.readline().split())))
K.sort()

temp = K[0]
result = 1

for i in range(1, N):
    if temp[1] > K[i][1]:
        temp = K[i]

    elif temp[1] <= K[i][0]:
        temp = K[i]
        result += 1

print(result)