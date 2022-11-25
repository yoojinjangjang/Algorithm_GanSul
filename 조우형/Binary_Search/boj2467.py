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
array.sort()

result = abs(array[-2] + array[-1])
ans = []

for i in range(len(array)):
    start = i+1
    end = len(array)-1

    while start >= end:
        mid = (start + end)//2

        total = abs(array[i]+array[mid])
        if total < result:
            total = result
            ans[0] = array[i]
            ans[1] = array[mid]















for i in range(len(array)):
    if i == len(array):
        break

    mid = ((i+1)+(len(array)-1))//2
    temp = abs(array[i] + array[mid])

    if temp < result:
        ans[0] = i
        ans[1] = mid









while start <= end:
    sum = 0
    mid = (start + end)//2

    if abs(array[start]+array[end]) < result:
        ans[0] = array[start]
        ans[1] = array[end]



