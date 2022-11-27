'''
Binary Search 기출 문제 29. 공유기 설치
집 N개가 수직선 위에 있다. 와이파이를 즐기기 위해 집에 공유기 C개를 설치하려고 한다.
한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를
가능한 크게 하여 설치하려고 한다.
C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
Ex) input
5 3
1
2
8
4
9

output = 3
'''
n, c = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

start = 1
end = array[-1]
result = 0

while start <= end:
    mid = (start + end)//2
    value = array[0]
    count = 1

    for i in range(1, n):
        if array[i] >= value + mid:
            count += 1
            value = array[i]

    if count < c:
        end = mid -1
    else:
        start = mid + 1
        result = mid

print(result)