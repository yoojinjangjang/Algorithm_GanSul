'''
구현 기출 문제 13 치킨 배달

집 : 1
치킨집 : 2
치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리
도시의 치킨 거리 : 모든 집의 치킨 거리의 합
'''
import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
city = []
house = []
chicken = []
for i in range(n):
    city.append(list(map(int,input().split())))

i = 0
for c in city:
    j = 0
    for k in c:
        if k == 1:
            house.append([i, j])
        elif k == 2:
            chicken.append([i, j])
        j += 1
    i += 1

m_chicken = list(combinations(chicken, m))

distance = 1e9
for m_c in m_chicken:
    sum = 0
    for h in house:
        temp = 1e9
        for c in m_c:
            d = abs(h[0] - c[0]) + abs(h[1] - c[1])
            temp = min(temp, d)
        sum += temp
    distance = min(distance, sum)

print(distance)