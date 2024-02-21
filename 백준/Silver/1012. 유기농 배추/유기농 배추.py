import sys
sys.setrecursionlimit(10000)

T = int(input())

def dfs(x, y):
    visited[x][y] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)
            
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    cnt = 0
    
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                cnt += 1

    print(cnt)