"""
백준 그리디 11047
가지고 있는 N 종류의 동전을 가지고 금액 K를 만들 때 필요한 동전의 개수

ex) N = 10 K = 4790
갖고 있는 동전 : 1 5 10 50 100 500 1000 5000 10000 50000

출력 : 12
"""
import sys

N, K = map(int, sys.stdin.readline().split())
coin = []
count = 0

for i in range(N):
    coin.append(int(sys.stdin.readline()))

coin.sort(reverse=True)

for i in coin:
    #if K//i != 0:
        count += K//i
        K %= i

print(count)
