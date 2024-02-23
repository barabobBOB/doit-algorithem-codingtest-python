import sys

def Count(length):
    cnt=0
    for x in snacks:
        if x>=length:               # 이부분을 생각못함 ㅠ이부분 추가 중요! 
            cnt+=(x//length)
    return cnt

if __name__=="__main__":
    M,N=map(int, input().split())               # 조카수:M, 과자의 수:N 
    snacks=list(map(int, input().split()))

    start=0
    end=sys.maxsize

    res=0
    while start<=end:
        mid=(start+end)//2
        if mid==0:       # 모든 조카에게 같은 길이의 막대과자를 나눠줄 수 없을 때
            break        
        if Count(mid)>=M:
            res=mid
            start=mid+1
        else:
            end=mid-1

    print(res)