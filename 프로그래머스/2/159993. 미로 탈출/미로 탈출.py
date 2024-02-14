from collections import deque

def solution(maps):
    def bfs(st, en) -> int:
        vis = [[0 for i in range(wid)] for j in range(hei)]
        Q = deque()
        Q.append(st)
        vis[st[0]][st[1]] = 1
        while Q:
            x, y = Q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= hei or ny >= wid: continue
                if maps[nx][ny] == 'X' or vis[nx][ny] != 0: continue
                vis[nx][ny] = vis[x][y] + 1
                Q.append((nx, ny))
        return vis[en[0]][en[1]] - 1

    hei = len(maps)
    wid = len(maps[0])    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(hei):
        for j in range(wid):
            if maps[i][j] == 'S': start = (i, j)
            elif maps[i][j] == 'L': lever = (i, j)
            elif maps[i][j] == 'E': end = (i, j)

    time1 = bfs(start, lever)
    if time1 == -1: return -1
    time2 = bfs(lever, end)
    if time2 == -1: return -1
    return time1 + time2

# def solution(maps):
#     answer = 0
    
#     len_maps = len(maps)
    
#     def bfs(sx, sy, ex, ey):
#         visited_cnt = [[0] * len_maps for _ in range(len_maps)]
#         visited_cnt[sy][sx] = 1
        
#         q = deque()
        
#         q.append((sx, sy))
        
#         dx = [0, 0, -1, 1]
#         dy = [-1, 1, 0, 0]
        
#         while q:
#             x, y = q.popleft()
                
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
                
#                 if nx < 0 or ny < 0 or nx >= len_maps or ny >= len_maps: continue
#                 if maps[ny][nx] == 'X' or visited_cnt[ny][nx] != 0: continue
                
#                 visited_cnt[ny][nx] = visited_cnt[y][x] + 1
#                 q.append((nx, ny))
        
#         return visited_cnt[ey][ex] - 1
    
#     sx, sy = 0, 0
#     lx, ly = 0, 0
#     ex, ey = 0, 0
    
#     c = 0
    
#     for i in range(len_maps):
#         if c == 3:
#             break
#         for j in range(len_maps):
#             if maps[i][j] == 'S':
#                 sx = j
#                 sy = i
#                 c += 1
#             elif maps[i][j] == 'L':
#                 lx = j
#                 ly = i
#                 c += 1
#             elif maps[i][j] == 'E':
#                 ex = j
#                 ey = i
#                 c += 1
    
#     cnt = 0
    
#     cnt = bfs(sx, sy, lx, ly)

#     if cnt == 0:
#         answer = -1
#     else:
#         cnt = bfs(sx, sy, ex, ey)
#         if cnt == 0:
#             answer = -1
#         else:
#             answer = cnt
    
#     return answer