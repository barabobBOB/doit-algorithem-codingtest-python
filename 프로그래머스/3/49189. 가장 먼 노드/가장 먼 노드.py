from collections import deque
INF = int(1e9)

def solution(n, edge):
    graph = {i:[] for i in range(1, n+1)}
    
    # 그래프 만들기
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
        
    q = deque([])
    
    # 초기에 도달할 수 없도록 설정
    distance = [INF] * (n+1)
    
    # 1부터 시작
    distance[1] = 0
    q.append(1)
    
    while q:
        now = q.popleft()
        
        # 해당하는 키에 속한 노드 탐색
        for i in graph[now]:
            
            # 무한이면 한번도 접근을 안한 것임
            if distance[i] == INF:
                # 거리 추가
                distance[i] = distance[now] + 1
                q.append(i)
                
    # 해당 리스트에서 가장 큰 값을 찾고 그 값이 포함된 값을 count 함수로 셈
    return distance[1:].count(max(distance[1:]))