n = int(input())
m = int(input())

nums = [[0 for _ in range(n)] for _ in range(n)]
answer = [n//2+1, n//2+1]

def draw():
    global n
    x = y = n//2
    cnt = num = 2
    d = [(0,1),(1,0),(0,-1),(-1,0)]
    t = 0
    nums[x][y] = 1
    x-=1
    y-=1

    while True:
        for _ in range(4):
            a, b = d[t]
            for _ in range(cnt):
                x += a
                y += b
                nums[x][y] = num
                if num == m:
                    answer[0] = x+1
                    answer[1] = y+1
                if num == n**2:
                    return
                num += 1
            t = (t+1)%4
        cnt += 2
        x -= 1
        y -= 1

draw()

for i in nums:
    print(*i)
print(*answer)