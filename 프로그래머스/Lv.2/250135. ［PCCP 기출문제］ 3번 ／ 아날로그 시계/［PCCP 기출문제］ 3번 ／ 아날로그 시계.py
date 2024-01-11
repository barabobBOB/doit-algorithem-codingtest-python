def convertToSecond(h,m,s):
    return 3600*h + m*60 + s

def solution(h1, m1, s1, h2, m2, s2):
    startTime, endTime = convertToSecond(h1,m1,s1), convertToSecond(h2,m2,s2)

    ring = {}

    # 초기화
    for t in range(convertToSecond(24,0,0)):
        ring[t] = {"cur":0,"after":0}


    # 이전 시각의 초침, 분침, 시침의 각도
    prevSecond, prevMinute, prevHour = 0, 0, 0

    for t in range(1,convertToSecond(24,0,0)):
        afterCount,curCount = 0,0

        # 현재 시각의 초침, 분침, 시침의 각도
        curSecond, curMinute, curHour = 6*t%360, (t/10)%360, (t/120)%360

        # 첫 번째 경우 : 초침이 분침을 따라 잡은 경우
        if  prevSecond < prevMinute and curSecond > curMinute :
            afterCount += 1
        # 두 번째 경우 : 초침이 분침을 따라 잡았지만 현재의 초침의 위치가 0이라 위의 if문에서 카운트 안된 경우
        elif prevSecond < prevMinute and curSecond == 0 :
            afterCount += 1
        # 세 번째 경우 : 초침이 분침과 현재 시각에 위치가 정확히 같은 경우
        elif curSecond == curMinute:
            curCount += 1

        # 첫 번째 경우 : 초침이 시침을 따라 잡은 경우
        if  prevSecond < prevHour and curSecond > curHour:
            afterCount += 1
        # 두 번째 경우 : 초침이 시침을 따라 잡았지만 현재의 초침의 위치가 0이라 위의 if문에서 카운트 안된 경우
        elif prevSecond < prevHour and curSecond == 0 :
            afterCount += 1
        # 세 번째 경우 : 초침이 시침과 현재 시각에 위치가 정확히 같은 경우
        elif curSecond == curHour:
            curCount += 1


        # t에 cur과 after를 각각 반영, 12시 0분 0초에 반영x
        if t != 3600 * 12:
            if curCount != 0:
                ring[t]["cur"] += curCount
            if afterCount != 0:
                ring[t-1]["after"] += afterCount

        # prev 업데이트
        prevSecond, prevMinute, prevHour = curSecond, curMinute, curHour

    # 0시 0분 0초와 12시 0분 0초는 한번만 울림
    ring[0] = {"cur": 1, "after": 0}
    ring[3600 * 12] = {"cur": 1, "after": 0}

    ret = 0

    for time in range(startTime,endTime):
        if time in ring:
            ret += ring[time]["after"]
            ret += ring[time]["cur"]

    ret += ring[endTime]["cur"]
    return ret