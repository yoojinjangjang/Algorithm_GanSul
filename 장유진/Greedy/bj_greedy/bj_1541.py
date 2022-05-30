'''
잃어버린 괄호: 양수,+,-,괄호를 가지고 만든 식의 괄호를 지움 괄호를 적절히 쳐서 최솟값을 만듦

입력 : 식 ( 0~9,+,- )
출력 : 최솟값 정답
'''

import sys
input = sys.stdin.readline

data = input().split('-')
for i in range(len(data)):
    addVal = list(map(int,data[i].split('+')))
    if i==0:
        res = sum(addVal)
        continue
    res -= sum(addVal)
print(res)