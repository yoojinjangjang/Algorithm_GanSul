"""
만들 수 없는 금액 : N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값 구하기

입력 : N ( 동전의 개수 )
      화폐 단위를 나타내는 N개의 자연수

출력 : 만들 수 없는 최솟값
"""

import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
data.sort()

target = 1
for i in data:
    if target < i:
        break
    target += i

print(target)