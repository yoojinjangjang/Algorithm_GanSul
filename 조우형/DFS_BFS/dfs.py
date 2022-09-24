def dfs(graph, start, visited):

    visited[start] = True

    print(start, end = " ")

    for i in graph[start]:
        if visited[i] == False:
            dfs(graph, i, visited)

def dfs2(graph, v, visited):

    visited[v] = True
    print(v,end=" ")
    for i in graph[v]:
        if visited[i] == False:
            dfs2(graph, i, visited)


def dfs_1(graph, v, visited):

    visited[v] = True
    print(v, end = " ")
    for i in graph[v]:
        if not visited[i]:
            dfs_1(graph, i, visited)



graph = [[],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]]
visited = [False]*9
dfs_1(graph, 1, visited) # dfs(그래프, 시작지점, 방문처리
