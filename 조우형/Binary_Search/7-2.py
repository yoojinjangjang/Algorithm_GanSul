'''
Binary Search 실전 문제 2. 부품 찾기

매장에 N개의 부품이 있다.
손님이 M개 종류의 부품을 대량 구매하겠다고 하면, 손님이 문의한 부품 M개 종류를 모두
확인해서 견적서를 작성해야 한다. 가게 안에 부품이 있는지 확인하는 프로그램을 작성하세요.
'''
def binary_search(target, arr, start, end):
    if start > end:
        return None

    mid = (start+end)//2

    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search(target, arr, start, mid-1)
    else:
        return binary_search(target, arr, mid+1, end)

n = int(input())
store = list(map(int, input().split()))
store.sort()
m = int(input())
req = list(map(int, input().split()))

for r in req:
    if binary_search(r, store, 0, n-1):
        print("yes", end=" ")
    else:
        print("no", end = " ")
