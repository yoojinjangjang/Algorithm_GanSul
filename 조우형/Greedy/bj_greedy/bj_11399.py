'''
백준 그리디 11399
ATM 앞에 N명의 사람들이 줄을 서 있다.
줄을 서 있는 사람 N과 각 사람이 돈을 인출하는데 걸리는 시간 P가 주어졌을 때,
각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을
작성하시오.

ex) N : 5
P : 3 1 4 3 2

출력 : 32
'''

n= int(input())
p = list(map(int, input().split()))
p.sort()
sum = 0
temp = 0

for i in range(n):
    temp += p[i]
    sum += temp

print(sum)