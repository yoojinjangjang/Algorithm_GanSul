'''
길이가 N인 정수 배열 A와 B -->  S = A[0] * B[0] +...+ A[N-1] * B[N-1]
S의 값을 가장 작게 만들기 위해 A의 수를 재배열
S의 최솟값을 출력

입력 : N ( 배열 길이 )
      A의 원소
      B의 원소
출력 : S의 최솟값
'''
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
res = 0
for i in a:
    res += i*max(b)
    b.remove(max(b))
print(res)