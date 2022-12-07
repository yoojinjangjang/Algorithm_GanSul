'''
Sort 기출 문제 24. 안테나

일직선상의 마을에 여러 채의 집이 위치해 있다. 이 중에서 특정 위치의 집에 한 개의 안테나를 설치하려고 한다.
안테나로부터 모든 집까지의 거리의 총합이 최소가 되도록 설치하려고 한다.
집들의 위치 값이 주어질 때, 안테나를 설치할 위치를 선택하는 프로그램을 작성하세요.

Ex)
input
4
5 1 7 9

output
5
'''
n = int(input())
homes = list(map(int, input().split()))

homes.sort()
start = 0
end = len(homes) - 1
mid = (start + end) //2
res = homes[mid]

sum = 0
for i in homes:
    sum += abs(homes[mid]-i)

while start <= end:
    temp = 0
    mid = (start + end) // 2

    for i in homes:
        temp += abs(homes[mid]+i)

    if sum > temp:
        res = homes[mid]
        sum = temp
        end = mid -1
    else:
        start = mid + 1

print(res)