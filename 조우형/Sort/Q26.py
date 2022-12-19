'''
정렬 Q26. 카드 정렬하기

정렬된 두 묶음의 숫자 카드가 있을 때 각 묶음의 카드의 수를 A, B라 하면
보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B번의 비교를 해야 합니다.
N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한 지를 구하는
프로그램을 작성하세요.
'''
import heapq

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

res = 0
while len(cards) != 1:

    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)

    sum = card1 + card2
    res += sum

    heapq.heappush(cards, sum)

print(res)



