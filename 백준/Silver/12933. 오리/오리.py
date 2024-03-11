quack = 'quack'
duck = input()
visited = [0] * len(duck)

def find(start):
    global cnt
    j = 0
    first = 1
    for i in range(start, len(duck)):
        if duck[i] == quack[j] and not visited[i]:
            visited[i] = 1
            if duck[i] == 'k':
                if first:
                    cnt += 1
                    first = 0
                j = 0
            
            else:
                j += 1

if len(duck) % 5 != 0:
    print(-1)
    exit()

cnt = 0
for i in range(len(duck)):
    if duck[i] == 'q' and not visited[i]:
        find(i)

if cnt == 0 or not all(visited):
    print(-1)

else:
    print(cnt)