'''
Q4-2] 시각
: 정수 N 입력, 00시 00분 00초 부터 N시 59분 59초 까지 3이 하나라도 포함되는 모든 경우의 수

입력 : 정수 N
출력 : 3이 하나라도 포함되는 모든 경우의 수

*답지봐버림*
'''
import sys
input = sys.stdin.readline

n = int(input())
count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)