n = int(input())
nums = list(map(int, input().split()))

JH_cash = n
SM_cash = n

JH_cnt = 0
SM_cnt = 0

for i in range(14):
    if JH_cash//nums[i] > 0:
        JH_cnt += JH_cash//nums[i]
        JH_cash -= (JH_cash//nums[i]) * nums[i]
        
for i in range(2, 13):
    # 성민이 주식 매수
    if nums[i-2] > nums[i-1] > nums[i]:
        cnt = SM_cash//nums[i+1]
        if SM_cash//nums[i+1] > 0:
            SM_cnt += cnt
            SM_cash -= (cnt * nums[i+1])
    # 성민이 주식 매도
    if nums[i-2] < nums[i-1] < nums[i]:
        SM_cash += (nums[i+1] * SM_cnt)
        SM_cnt = 0

if JH_cash + JH_cnt*nums[-1] > SM_cash + SM_cnt*nums[-1]:
    print("BNP")
elif JH_cash + JH_cnt*nums[-1] < SM_cash + SM_cnt*nums[-1]:
    print("TIMING")
else:
    print("SAMESAME")