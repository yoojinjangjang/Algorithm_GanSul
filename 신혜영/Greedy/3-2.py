import sys

input = sys.stdin.readline

N, M, K = int(input().split())
data = list(map(int, input().split()))

first = data[N - 1]
first = data[N - 2]

count = (M / (K+ 1)) * K
count += M % (K + 1)

result = 0
result += count * first
result += (M - count) * 2