'''
그리디 기출 문제 1. 모험가 길드
한 마을에 모험가 N명이 있습니다. 공포도가 X인 모험가는 반드시 X명 이상으로 구성한
모험가 그룹에 참여해야합니다.

N : 각자의 공포도를 지닌 모험가의 리스트
count : 최대 그룹의 수
'''

num = int(input("모험가 수 : "))
n = list(map(int, input("모험가의 공포도 : ").split()))
n.sort(reverse=True)
count = 0

while len(n) != 0:
    temp = n[0]
    # print("현재 남은 멤버는 ", n)
    # print("이번 그룹 멤버는 ", n[:temp])
    n = n[temp:]
    count += 1

print(count)

'''
모험에 참여하지 않아도 되기 때문에 공포도가 높은 것부터
그룹을 결성하는 것보다, 공포도가 높은 사람은 모험에 참여시키지 않는
방향으로 하여, 공포도가 낮은 모험가부터 그룹을 결성하는 것이
최대 그룹을 형성할 수 있다.
ex) 1 1 1 1 5

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
'''