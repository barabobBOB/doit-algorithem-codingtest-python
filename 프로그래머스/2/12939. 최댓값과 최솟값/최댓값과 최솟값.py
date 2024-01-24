def solution(s):
    answer = ''
    
    nums = list(map(int, s.split(' ')))
    max_num = nums[0]
    min_num = nums[0]
    
    for i in nums:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
    
    answer+=str(min_num)
    answer+=' '
    answer+=str(max_num)
    
    return answer