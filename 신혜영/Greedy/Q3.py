'''
전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에서 더 작은 횟수를 가지는 경우를 계산
'''
import sys

S = sys.stdin.readline().strip()
cnt0 = 0

for i in range(1, len(S) - 1):
    if S[i-1:i] != S[i] and S[i] == S[i:i+1]:
        cnt0 += 1
        break

print(cnt0)

