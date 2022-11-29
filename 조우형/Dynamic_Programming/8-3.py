'''
Dynamic Programming 실전 문제 3. 개미 전사

일직선으로 나열된 식량 창고에서 식량을 뺏어오려고 한다. 인접한 식략 창고를
공격하면 정찰병들이 알아챈다.
정찰병들이 알아채지 않도록 식량 창고에서 약탈할 수 있는 식량의 최대값을 구하세요.
Ex) input
4
1 3 1 5

output
8
'''
n = int(input())
foods = list(map(int, input().split()))

d = [0]*100
d[0] = foods[0]
d[1] = max(d[0], foods[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+foods[i])

print(d[n-1])