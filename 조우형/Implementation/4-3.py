'''
구현 실전 문제 3. 왕실의 나이트
8 x 8 체스판 위에 나이트가 특정한 위치에 위치해 있다.
나이트는 다음과 같이만 움직일 수 있다.
1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

나이트의 위치가 주어졌을 때, 나이트가 한 번 움직여서 이동할 수 있는 경우의 수를 구하여라.

Ex) a1 에 있을 때 이동할 수 있는 경우의 수는
1. 오른쪽으로 두 칸 이동 후 아래로 한 칸 이동하기 - c2
2. 아래로 두 칸 이동 후 오른쪽으로 한 칸 이동하기 - b3
'''
import sys
input = sys.stdin.readline()
low = ord(input[0]) - ord('a') + 1
col = int(input[1])

'''
답안 예시
dx, dy 대신 
steps = [(-2, -1), (-1,-2), (1,-2) ......]
로 정의해서 해결하였다. 두 방법 모두 자주 사용되므로, 참고하도록 하자.
'''
dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]
cnt = 0

for i in range(8):

    temp_low = low + dx[i]
    temp_col = col + dy[i]

    if temp_low > 8 or temp_low < 1 or temp_col >8 or temp_col < 1:
        continue

    cnt += 1

print(cnt)
