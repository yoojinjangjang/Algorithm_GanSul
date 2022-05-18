"""
만들 수 없는 금액 : N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값 구하기

입력 : N ( 동전의 개수 )
      화폐 단위를 나타내는 N개의 자연수

출력 : 만들 수 없는 최솟값
"""

n = int(input())
data = list(map(int, input().split()))
data.sort()

ans = 1
for x in data:
    if ans<x:
        break
    ans += x

print(ans)