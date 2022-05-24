'''
그리디 기출 문제 6. 무지의 먹방 라이브
1번부터 N번까지의 음식을 섭취하는데 일정 시간이 소요됩니다.
음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취합니다.
먹방을 시작한지 k초 후에 네트워크 장애로 인해 방송이 중단되었습니다.
네트워크 정상화 후 다시 음식을 섭취할 때, 몇 번 음식을 섭취하고 있어야 할까요.

food_time = [3,1,2] 음식 3개의 각각 걸리는 시간
k = 5   방송이 중단된 시간
result = 1  먹고 있어야 하는 음식 번호
'''

# food_times = list(map(int, input("음식 먹는데 소요되는 시간 : ").split()))
# k = int(input("방송 중단 시간 : "))
food_times= [3,1,2]
k = 5

def solution(food_times, k):

    i = 0
    cnt = 0
    answer = 0
    while cnt <= k or answer != 0:
        i = (len(food_times) + i) % len(food_times)

        if food_times.count(0) == len(food_times):
            answer = -1

        if food_times[i] != 0:
            if cnt >= k:
                answer = i+1
                break
            food_times[i] -= 1
            i += 1
            cnt +=1



        else:
            i += 1

    return answer

print(solution(food_times,k))
