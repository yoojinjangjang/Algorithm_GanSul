'''
일반적으로 방향을 설정해서 이동하는 문제유형에서는 dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적이다. 
'''
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

# 현재 캐릭터의 X좌표, Y좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 방문처리

# 전체 맵 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 1단계
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 가본적 없고, 육지인 곳
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        # 가본 곳 체크
        d[nx][ny] = 1
        # 이동
        x = nx
        y = ny
        
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    # 3단계 네 방향 모두 가본 칸 
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 후진
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤쪽 방향이 바다로 되어있는 경우
        else:
            break
        turn_time = 0

print(count)