def solution(food_times, k):
    result = 0
    time_cnt = 0
    food_cnt = 0

    while k > 0:

        while food_times[result] == 0:
            if result >= len(food_times):
                result = 0
            else:
                result += 1

            food_cnt += 1
            if food_cnt + 1 == len(food_times):
                return -1

        food_times[result] -= 1

        print(
            "{0} ~ {1}초 동안에 {2}번 음식을 섬취한다. 남은시간은 {3}입니다.".format(
                time_cnt, time_cnt + 1, result + 1, food_times
            )
        )

        time_cnt += 1
        k -= 1

        if result < len(food_times) - 1:
            result += 1
        else:
            result = 0
    return result + 1


food_times = list(map(int, input().split()))
k = int(input())

result = solution(food_times, k)

if result == -1:
    print("남은 음식이 없습니다.")
else:
    print(
        "{0}초에서 네트워크 장애가 발생했습니다. {1}번 음식을 섭취해야 할 때 중단되었으므로, 장애 복구 후에 {1}번 음식부터 다시 먹기 시작하면 됩니다.".format(
            k, result
        )
    )
