'''
구현 기출 문제 7. 럭키 스트레이트
필살기 '럭키 스트라이크'는 특정 점수 조건을 만족할 때만 사용할 수 있습니다.
자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과
오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미합니다.

Ex) N = 123402
Result = LUCKY
'''
import sys
n = sys.stdin.readline()
k = int(len(n) / 2)
cnt = 0

sum1 = 0
sum2 = 0
for i in range(k):
    sum1 += int(n[i])
for i in range(k,len(n)-1):
    sum2 += int(n[i])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")
