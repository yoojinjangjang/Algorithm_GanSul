'''
Binary Search 백준 2467. 용액

두 용액을 섞어서 0에 가까운 값을 갖게 되는 두 용액을 구하세요.
0에 가까운 값을 만들어내는 용액이 2개 이상인 경우에는 아무거나 구하세요.
Ex)
n = 5
list = [-99, -2, -1, 4, 98]
'''
n = int(input())
array = list(map(int, input().split()))

sort(array)
start = 0
end = len(sort) - 1

result = 1e9
ans = []
while start <= end:
    sum = 0
    mid = (start + end)//2

    if abs(array[start]+array[end]) < result:
        ans[0] = array[start]
        ans[1] = array[end]



