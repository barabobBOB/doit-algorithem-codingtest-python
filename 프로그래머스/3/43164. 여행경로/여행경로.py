from collections import defaultdict

def solution(tickets):
    # 특정 티켓의 인접 리스트를 구하는 함수
    def init_graph():
        routes = defaultdict(list)
        for key, value in tickets:
            routes[key].append(value)
        for r in routes:
            routes[r].sort(reverse=True)  # 뒤집어서 pop을 사용할 때 알파벳 순으로 가장 앞서는 경로를 선택
        return routes

    # 재귀를 사용한 DFS
    def dfs(airport, path):
        # 모든 티켓을 사용할 때까지 경로를 탐색
        while routes[airport]:
            next_airport = routes[airport].pop()  # 알파벳 순으로 가장 앞서는 경로 선택
            dfs(next_airport, path)
        path.append(airport)

    routes = init_graph()
    path = []
    dfs("ICN", path)

    return path[::-1]  # 경로를 뒤집어서 반환
