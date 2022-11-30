'''
Dynamic Programming 실전 문제 5. 효율적인 화폐 구성

N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
각 화폐는 몇 개라도 사용할 수 있으며, 순서만 다른 것은 같은 경우로 구분한다.

n = 100개, m = 10000개이므로, n x m은 백만개밖에 되지 않으므로 for문 두 개로 해결할 수 있다.

Ex) input
n = 2 m = 15
2
3

output = 5
'''
n, m = map(int, input().split())

moneys = []
for _ in range(n):
    moneys.append(int(input()))

d = [10001]* (m+1)

d[0] = 0
for i in moneys:
    for j in range(i, m+1):
        if d[j-i] != 10001: # 숫자를 더하기 이전 값이 10001이라는 것은 해당 숫자에 도달하는 경우의 수가 없으므로, 없다면 구해볼 필요가 없다.
            d[j] = min(d[j], d[j-i]+1) #j원이 되기 위한 경우의 수와 더하기 이전 값의 경우의 수 중 최솟값으로 지정

if d[m] == 10001:
    print(-1)
else:
    print(d[m])




