'''
Binary_Search 기출 문제 27. 정렬된 배열에서 특정 수의 개수 구하기

N개의 원소를 포함하고 있는 정렬된 수열에서 x가 등장하는 횟수를 계산하세요.
x인 원소가 하나도 없다면 -1을 출력하세요.
Ex)
array = {1,1,2,2,2,2,3}
target = 2
output = 4

array = {1,1,2,2,2,2,3}
target = 4
output = -1
'''
def binary_search(target, array, start, end):
    sum = 0
    if start > end:
        return 0

    mid = (start+end)//2

    if array[mid] == target:
        sum += 1

    sum += binary_search(target, array, start, mid-1)
    sum += binary_search(target, array, mid+1, end)

    return sum

n, x = map(int, input().split())
sequence = list(map(int, input().split()))
res = binary_search(x, sequence, 0, n-1)
if res == 0:
    print(-1)
else:
    print(res)
