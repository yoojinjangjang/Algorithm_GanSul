'''
Q4-4] 게임 개발
: N*M 크기의 정사각형, 각 칸은 육지 또는 바다
: 맵의 각 칸은 (A,B) / A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수
: 상하좌우 이동 가능, 바다는 갈 수 없다.
: - 현재 위치에서 왼쪽방향으로부터 차례대로 갈 곳을 정한다.
: - 왼쪽 방향에 아직 가보지 않은 칸 존재시 왼쪽 회준 후 한 칸 전진, 없다면 회전만 수행 후 1단계 돌아가기
: - 모두 가본 칸 이거나 바다인 경우 바라보는 방향 유지후 한 칸 뒤로 가고 1단계로 돌아가기 ( 뒤칸이 바다인 경우 움직임 멈춤 )
: 매뉴얼 따라 캐릭터 이동 후 방문한 칸의 수를 출력

입력 : 맵 세로 N 가로 M
: 게임 캐릭터가 있는 칸의 좌표 (A,B) 바라보는 방향 d ( 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽 )
: 맵이 육지인지 바다인지에 대한 정보 ( 0 : 육지, 1 : 바다 ) , 외곽은 항상 바다(1)

출력 : 이동을 마친 후 캐릭터가 방문한 칸의 수
'''

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a,b,d = map(int,input().split())
maps = [0] * n
for i in range(n):
    maps[i] = list(map(int,input().split()))

loc = [(-1,0),(0,1),(1,0),(0,-1)] # 북/동/남/서 의 좌표 변화 양
count = 0
maps[a][b] = 2
while True:
    prev_a = a
    prev_b = b
    for i in range(4):
        next_a = a+loc[d][0]
        next_b = b+loc[d][1]
        if maps[next_a][next_b] != 1 and maps[next_a][next_b] != 2:
            a = next_a
            b = next_b
            count += 1
            maps[a][b] = 2
            print(a,b)
            break
        d = (d+1)%4
    if prev_a == a and prev_b == b:
        next_a = a + loc[(d+2)%4][0]
        next_b = b + loc[(d+2)%4][1]
        if maps[next_a][next_b] == 1:
            break
        a = next_a
        b = next_b
        count += 1
        print(a,b)
print(count)
