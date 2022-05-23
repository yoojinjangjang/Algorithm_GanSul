'''
볼링공 고르기: 무게가 다른 볼링공을 고르려고 한다. 1~M 무게의 볼링공 N개 중 두사람이 고를 수 있는 볼링공 번호의 조합을 구하라

입력 : 볼링공 개수 N, 공의 최대 무게 M
      각 볼링공의 무게 K 리스트

출력 : 두 사람이 볼링공을 고르는 경우의 수
'''

n,m = map(int,input().split())
k = list(map(int,input().split()))

count = 0
for i in range(n):
    for j in range(i+1,n):
        if k[i] != k[j]:
            count += 1

print(count)