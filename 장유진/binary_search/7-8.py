import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rice_cakes = list(map(int, input().split()))
rice_cakes.sort()
max_rice_cake = rice_cakes[len(rice_cakes)-1]  # 최대 떡 길이


def find_max_cutting_rice_cake_cm(rice_cakes, cm, start, end, result):
    if start > end:
        return result
    mid_cm = (start + end) // 2
    cutting_rice_cakes = 0

    for rice_cake in rice_cakes:
        cutting_cm = rice_cake - mid_cm
        if cutting_cm > 0:
            cutting_rice_cakes += cutting_cm

    if cutting_rice_cakes >= cm:
        result = mid_cm
        return find_max_cutting_rice_cake_cm(rice_cakes, cm, mid_cm + 1, end, result)
    else:
        return find_max_cutting_rice_cake_cm(rice_cakes, cm, start, mid_cm - 1, result)


result = 0
print(find_max_cutting_rice_cake_cm(rice_cakes, M, 0, max_rice_cake, result))
