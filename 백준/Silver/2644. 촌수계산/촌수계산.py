from collections import deque

n = int(input())
A, B = map(int,input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
res = [0] * (n+1)


for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    visited[v] = True
    q = deque()
    q.append(v)
    
    while q:
        n = q.popleft()
        if n == B:
            return
        
        for i in graph[n]:
            if not visited[i]:
                visited[i] = True
                res[i] = res[n] + 1
                q.append(i)

bfs(A)
if res[B]>0:
    print(res[B])
else:
    print(-1)