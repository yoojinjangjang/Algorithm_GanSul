import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    hq = []
    for i in range(len(food_times)):
        heapq.heappush(hq, (food_times[i], i + 1))

    sum_of_times = 0
    prev = 0
    length = len(food_times)

    while True:
        if sum_of_times + (hq[0][0] - prev) * length >= k:
            break
        now = heapq.heappop(hq)
        sum_of_times += (now[0] - prev) * length
        length -= 1
        prev = now[0]

    hq.sort(key=lambda x: x[1])  # 번호를 기준으로 정렬
    k -= sum_of_times
    answer = hq[k % length][1]
    return answer