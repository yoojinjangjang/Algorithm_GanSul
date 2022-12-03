import heapq

N = int(input())
cards = []
compare_sum = 0

for i in range(N):
    heapq.heappush(cards, int(input()))

if N == 1:
    print(0)
else:
    while len(cards) > 1:
        compare_now = heapq.heappop(cards) + heapq.heappop(cards)
        compare_sum += compare_now
        heapq.heappush(cards, compare_now)
    print(compare_sum)
