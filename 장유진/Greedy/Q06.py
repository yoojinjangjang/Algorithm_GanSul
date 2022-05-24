'''
무지의 먹방 라이브
입력: food_times ( 음식 모두 먹는데 필요한 시간 ) , k ( 방송 중단 시간 )
출력 : 다시 섭취할 음식 번호
'''


def solution(food_times, k):
    answer = 0

    while True:
        count = len(food_times) - food_times.count(0)
        if count > k:
            break
        elif count == 0:
            return -1
        k -= count
        for i in range(len(food_times)):
            if food_times[i] != 0:
                food_times[i] -= 1
        print(food_times)
        print(k, 'count = ', count)

    print(food_times)
    print(k)
    for i in range(len(food_times)):
        if food_times[i] != 0 and k == 0:
            return i + 1
        if food_times[i] != 0:
            k -= 1


print('answer = ', solution([3, 1, 0, 5, 2], 10))
print('--------------------')
print('answer = ', solution([3, 1, 2], 5))
