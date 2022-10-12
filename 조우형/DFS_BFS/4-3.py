'''
DFS_BFS/BFS 실전 문제 3. 음료수 얼려 먹기
N x M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 생성되는 총 아이스크림의 개수를 구하여라.

Ex)
4 5
00110
00011
11111
00000

result = 8
'''
import sys
n, m = map(int, sys.stdin.readline().split())
frames = []
result = 0
for i in range(n):
    frames.append(list(map(int, input())))

# def 사용해서 재귀로 풀어보는게 맞을듯 dfs 로 풀도록 하자.
def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if frames[x][y] == 0:
        frames[x][y] = 1 #방문한 곳이기 때문에 1로 처리하여 재방문 x로 만듦
        dfs(x-1,y) #인덱스가 범위를 벗어나더라도 위에 조건문에서 처리해주기 때문에 괜찮음 그래서 필요했구만 위 조건문은
        dfs(x, y-1)
        dfs(x+1,y)
        dfs(x, y+1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)

    