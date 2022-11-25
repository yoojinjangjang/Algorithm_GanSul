'''
Binary Search 기출 문제 28. 고정점 찾기
고정점이란, 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미합니다.
N개의 원소를 갖는 수열에서 고정점을 찾으세요.

Ex)
N = 5
Array = [-15, -4, 2, 8, 13]

output = 2
'''
n = int(input())
array = list(map(int, input().split()))

start = 0
end = len(array) -1
result = -1

while start <= end:
    mid = (start+end)//2
    #print(mid)
    if mid == array[mid]:
        result = mid
        break

    if mid < array[mid]:
        end = mid-1
    else:
        start = mid + 1


print(result)
