import sys
sys.setrecursionlimit(1_000_000)

# 가로 M, 세로 N
N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N)]

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M or visited[x][y] or graph[x][y] == 0:
        return 0

    visited[x][y] = True
    area = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        area += dfs(nx, ny)
        
    return area

cnt = 0
result = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] == 1:
            area = dfs(i, j)
            if area > 0:
                cnt += 1
                result = max(area, result)

print(cnt)
print(result)