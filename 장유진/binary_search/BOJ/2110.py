import sys
input = sys.stdin.readline


def binary_search(start, end):
    answer = 0
    while start <= end:
        mid = (start+end) // 2
        current = house[0]
        count = 1

        for i in range(1, len(house)):
            if house[i] >= current + mid:
                current = house[i]
                count += 1

        if count >= C:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    return answer


N, C = map(int, input().split())
house = [int(input()) for i in range(N)]
house.sort()

start = 1
end = house[-1] - house[0]
print(binary_search(start, end))
