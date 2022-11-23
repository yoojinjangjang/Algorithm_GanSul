'''
swea 1244. 최대 상금
'''
T = int(input())
for test_case in (1, T+1):
    numbers = list(map(int, input()))
    ex = int(input())

    for i in range(ex):
        