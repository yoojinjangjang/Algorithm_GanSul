'''
무지의 먹방 라이브
입력: food_times ( 음식 모두 먹는데 필요한 시간 ) , k ( 방송 중단 시간 )
출력 : 다시 섭취할 음식 번호
'''


def solution(food_times, k):
    idx = 0
    n = len(food_times)
    for i in range(k):
        count = 0
        while food_times[idx % n] == 0:
            idx += 1
            count += 1
            print(food_times)
            print(count)
            if count > n+1:
                return -1

        print(food_times)
        food_times[idx % n] -= 1
        idx += 1

    if food_times[(idx % len(food_times))] == 0:
        return -1
    else:
        return idx % len(food_times)+1

print(solution([3,1,0,5,2],10))