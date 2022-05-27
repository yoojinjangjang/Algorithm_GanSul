'''
동전 0 : 동전의 종류가 총 N 종류, 각각의 동전을 매우 많이 가지고 있다. 동전을 적절히 사용하여 그 가치의 합을 K로 만들고 싶다.
필요한 동전의 최소 갯수를 구하라.

입력: N ( 동전의 종류 수 ) , K ( 만들 가치 )
    N개의 줄에 각 동전의 가치가 오름차순으로 주어진다.

출력 : 필요한 동전의 최소 갯수
'''
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = [0] * n
for i in range(n):
    coin[i] = int(input())
coin.sort(reverse=True)
count = 0
for i in coin:
    if k <= 0:
        break
    if i <= k:
        count += k // i
        k %= i
print(count)