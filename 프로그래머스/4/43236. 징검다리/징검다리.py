def solution(distance, rocks, n):
    rocks.sort()
    l = len(rocks)

    start = 0
    end = distance

    while start <= end:
        # 현재 탐색 중인 돌 사이의 최소 거리
        mid = (start + end) // 2
        # 이전 돌
        prev = 0
        # 제거 해야 하는 돌
        count = 0

        for i in range(l):
            if rocks[i] - prev < mid:
                count += 1
            else:
                prev = rocks[i]

        if distance - prev < mid:
            count += 1

        if count > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer
