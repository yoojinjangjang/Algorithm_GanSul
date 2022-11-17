'''
Sort 실전 문제 3. 떡볶이 떡 만들기


'''
def binary_search(target, arr, start, end):
    sum = 0
    if start > end:
        return None

    mid = (start+end)//2

    for i in arr:
        if i > mid:
            sum += i - mid

    if sum == target:
        return mid

    if sum < target:
        return binary_search(target, arr, start, mid-1)
    else:
        return binary_search(target, arr, mid+1, end)


n, m = map(int, input().split())
dduck = list(map(int, input().split()))
dduck.sort()
print(binary_search(m, dduck, 0, dduck[-1]))
