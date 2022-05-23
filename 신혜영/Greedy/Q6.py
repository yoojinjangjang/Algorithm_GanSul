def solution(food_times, k):
    index = 0
    sec = 0
    
    while True:
        for food in food_times:
            if sec == k: break 

            if food != 0:
                food_times[index] -= 1
                answer = index
            sec += 1
            index = (index + 1) % len(food_times)
        if sec == k: break 
    return answer + 1


if __name__ == '__main__':
    print(solution([3,1,2], 5))