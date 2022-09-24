'''
DFS/BFS 실전 문제 3. 음료수 얼려 먹기

'''
import sys
n, m = map(int, sys.stdin.readline().split())
frames = [[]]
for i in range(n):
    frames.append(list(map(int, sys.stdin.readline().split())))

# def 사용해서 재귀로 풀어보는게 맞을듯 dfs 로 풀도록 하자.
for i in range(n):
    for j in range(m):
        if frames[i][j] == 0:





print(frame)

    