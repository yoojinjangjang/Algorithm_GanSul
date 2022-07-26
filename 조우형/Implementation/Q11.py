'''
구현 기출 문제 11. 뱀
N x N 게임판 위에 뱀이 0, 0 위치에서 출발하여 움직인다.
게임판에서 사과를 먹으면 길이가 1씩 늘어난다. 뱀이 이리저리 움직이다가
벽 또는 자기 자신의 몸과 부딪히면 게임은 종료된다.

Ex) 입력은 N(게임판 크기), K(사과의 개수), 사과의 위치, L(뱀의 방향 변환 횟수), 누적 시간 방향 정보로
이루어진다.

게임이 종료되는 시간을 출력하세요.
'''


apple = [] #사과 위치
d_info = [] # 방향(direction) 정보
time = 0
snake = [0, 0] #뱀의 현재 머리 위치

dx = [-1, 0, 1, 0] #방향 변환을 위한 좌표
dy = [0, 1, 0, -1]
d = 1

n = int(input()) #map의 크기
k = int(input()) #사과의 개수

for i in range(k): #사과의 위치 받는 부분
    x, y = map(int, input().split())
    apple.append([x-1, y-1])

l = int(input()) #방향 변환 횟수

for i in range(l):
    x, y = input().split()
    d_info.append([int(x), y])

arr = [] #뱀의 몸이 머무르고 있는 위치
arr.append(snake) #초기 위치 담기

while True:
    x = snake[0] + dx[d]
    y = snake[1] + dy[d]

    if n > x >= 0 and n > y >= 0 and [x, y] not in arr: #뱀이 벽이나 자신의 몸과 충돌 여부를 판단
        if [x, y] in apple: #사과 위치에 뱀의 머리가 방문했으면 리스트에서 삭제
            apple.remove([x, y])
        else: #사과를 방문하지 않았으면 길이가 늘어나지 않으므로 꼬리를 삭제
            arr.pop(0)

        arr.append([x, y])
    else:
        time += 1
        break

    time += 1

    snake = [x, y]

    for i in d_info:
        t = i[0] #현재 시간
        if time == t:
            if i[1] == 'D': #방향이 오른쪽
                d = (d+1) % 4
            elif i[1] == 'L':
                d = (d-1) % 4

print(time)