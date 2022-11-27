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

start = 0
end = n - 1
max_Num = 2e9 + 1
result = []

while start < end:
    total = array[start] + array[end]
    if abs(total) < max_Num:
        max_Num = abs(total)
        result = [array[start], array[end]]

    if total < 0:
        start = start + 1
    else:
        end = end-1

print("{} {}".format(result[0], result[1]))