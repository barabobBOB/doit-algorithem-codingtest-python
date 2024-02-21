N = int(input())

for _ in range(N):
    M = int(input())
    
    if M <= 3:
        print(1)
    else:
        d = [0] * (M+1)

        d[1] = 1
        d[2] = 1
        d[3] = 1
        
        for i in range(4, M + 1):
            d[i] = d[i - 2] + d[i - 3]
            
        print(d[-1])