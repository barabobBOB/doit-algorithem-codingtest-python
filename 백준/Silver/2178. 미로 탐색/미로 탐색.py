# import sys
# sys.setrecursionlimit(1_000_000)

from collections import deque

# 가로 M, 세로 N
N, M = map(int, input().split())

graph = [list(map(int, list(input()))) for _ in range(N)]
    
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited[x][y] = True
    
    q = deque()
    q.append((x, y))
    
    while q:
        mx, my = q.popleft()
        
        for i in range(4):
            nx = mx + dx[i]
            ny = my + dy[i]
                
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    graph[nx][ny] = graph[mx][my] + 1
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return graph[N - 1][M - 1]

print(bfs(0, 0))