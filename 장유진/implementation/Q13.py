'''
Q13: 치킨 배달
https://velog.io/@yoojinjangjang/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%B0%B1%EC%A4%80-15686
'''
import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())

city = []
home = []
chicken  = []
for i in range(n):
    city.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append([i+1,j+1])
        elif city[i][j] == 2:
            chicken.append([i+1,j+1])
min_distance = 100

for c in combinations(chicken,m):
    city_distance = 0
    for h in home:
        distance = 100
        for chick in c:
            if distance>abs(h[0]-chick[0]) + abs(h[1]-chick[1]):distance = abs(h[0]-chick[0]) + abs(h[1]-chick[1])
        city_distance += distance
    if min_distance > city_distance: min_distance = city_distance
print(min_distance)

