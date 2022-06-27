import sys

input = sys.stdin.readline

N = int(input())
meetroom = [list(map(int, input().strip().split())) for i in range(N)]
meetroom.sort(key=lambda x:x[0])
meetroom.sort(key=lambda x:x[1])

result = 1
end = meetroom[0][1]
for i in range(1, N):
    if end <= meetroom[i][0]:
        end = meetroom[i][1]
        result += 1

print(result)