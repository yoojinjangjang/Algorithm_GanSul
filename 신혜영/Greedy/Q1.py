import sys
from tkinter import X

input = sys.stdin.readline

N = int(input())
X_list = list(map(int, input().split()))
group = []
cnt = 0
X_list = sorted(X_list)

for x in X_list:
    cnt += 1
    if x <= cnt:
        group.append(x)
        cnt = 0

print(len(group))