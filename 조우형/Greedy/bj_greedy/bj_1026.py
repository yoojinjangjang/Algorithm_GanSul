'''
백준 그리디 1026
길이가 N인 정수 배열 A와 B가 있다.
S = A[0] X B[0] + ... + A[N-1] X B[N-1] 일 때,
S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자.
단, B에 있는 수는 재배열하면 안된다.
S의 최솟값을 출력하는 프로그램을 작성하시오.

Ex) N =5 (배열의 크기)
A = 1 1 1 6 0
B = 2 7 8 3 1

출력 : 18
'''
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
S = 0
a.sort()

for i in a:
    S += i * max(b)
    b.remove(max(b))
print(S)
