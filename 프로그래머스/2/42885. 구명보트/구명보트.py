from collections import deque

def solution(people, limit):
    people.sort()
    
    queue = deque()
    for p in people:
        queue.append(p)
    
    L = []
    count = 0
    
    while queue:
        if len(queue) > 1:
            min = queue.popleft()
            max = queue.pop()
            
            if min + max > limit:
                L.append(max)
                queue.appendleft(min)
            else:
                count += 1
        else:
            queue.popleft()
            count += 1
        
    return count + len(L)