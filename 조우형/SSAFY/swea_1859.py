'''
swea 1859. 백만 장자 프로젝트
n = 날짜
list = 날짜 별 시세

test1)
3
10 7 6

3
3 5 9

5
1 1 3 1 2
'''
n = int(input())
price = list(map(int, input().split()))

temp = []
idx = 0
while True:
    max_num = max(price[idx:])
    co = price[idx:]
    for i in range(len(price[idx:])):
        if price