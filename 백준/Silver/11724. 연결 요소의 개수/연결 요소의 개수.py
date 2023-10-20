import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m  = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)

cut = 0

for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        cut += 1

print(cut)