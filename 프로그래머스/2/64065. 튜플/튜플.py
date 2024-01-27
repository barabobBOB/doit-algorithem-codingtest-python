def solution(s):
    answer = []
    s = s[:-2].replace('{','').replace(',',' ').split('}')
    
    s = [i.split() for i in s]
    
    s.sort(key=lambda x:len(x))
	
    for tup in s:
        diff = set(tup) - set(answer)
        answer.append(list(diff)[0])
    
    answer = [int(i) for i in answer]
    
    return answer