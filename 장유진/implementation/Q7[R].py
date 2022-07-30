'''
Q07: 럭키 스트레이트(321p)
점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황
--> 럭키 스트레이트 기술 사용

입력: 점수 N ( 항상 짝수 자릿수 )
출력: 사용 가능 시 LUCKY, 사용 불가 시 READY

'''
import sys
input = sys.stdin.readline

n = input()

result = "LUCKY" if sum(map(int,n[:len(n)//2])) == sum(map(int,n[len(n)//2:len(n)-1])) else "READY"

print(result)