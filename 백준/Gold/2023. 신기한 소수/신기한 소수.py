n = int(input())
    
result = []
    
def is_prime(text):
    for i in range(2, int(text / 2 + 1)):
        if text % i == 0:
            return False
    return True
    
def dfs(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(1, 10):
            if i % num == 0:
                continue
            if is_prime(num * 10 + i):
                dfs(num * 10 + i) 
                
dfs(2)
dfs(3)
dfs(5)
dfs(7)