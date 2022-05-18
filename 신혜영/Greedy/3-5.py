import sys

input = sys.stdin.readline

N, K = map(int, input().split())
result = 0

# K로 최대한 많이 나눌 수 있도록 하는 것이 최적의 해를 보장하는 것이다. 
while N >= K:
    while N % K != 0:
        N -= 1
        result += 1

    N //= K
    result += 1    

# 마지막으로 남은 수에 대하여 1씩 빼기
while N > 1:
    N -= 1
    result += 1

print(result)