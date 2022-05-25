'''
ATM : N명의 사람 중 i번째 사람이 돈을 인출하는 시간 Pi분
사람들이 줄을 서는 순서에 따라 필요한 시간의 합이 달라지게 된다. 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하라

입력 : 사람의 수 N
      각 사람이 돈을 인출하는데 걸리는 시간 P
출력 : 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값
'''

import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int,input().split()))
p.sort()
sum = 0
result = 0
for i in p:
    sum += i
    result += sum
print(result)