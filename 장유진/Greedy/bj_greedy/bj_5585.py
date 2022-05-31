'''
거스름돈 : 잔돈으로 500,100,50,10,5,1
        거스름돈 개수가 가장 적게 잔돈을 준다. 물건을 사고 잔돈의 개수를 구하라

입력 : 지불한 돈
출력 : 잔돈에 포함된 매수
'''

import sys
input = sys.stdin.readline

data = int(input())
data = 1000 - data
coin = [500,100,50,10,5,1]
count = 0

for i in coin:
    if data <= 0:
        break
    if i <= data:
        count += data//i
        data %= i
print(count)