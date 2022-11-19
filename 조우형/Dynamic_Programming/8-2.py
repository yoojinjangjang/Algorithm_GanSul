'''
Dynamic Programming 실전 문제 2. 1로 만들기

'''
n = int(input())

def dp():
    pass
if n == 1:
    n = n
if n%5 == 0:
    n = n/5

if n%3 == 0:
    n = n/3

if n%2 == 0:
    n = n/2