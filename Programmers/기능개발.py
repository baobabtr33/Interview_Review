import math

def solution(progresses, speeds):
    answer = []
    days = []
    for i, j in zip(progresses, speeds): 
        tmp = math.ceil((100 - i) / j)
        days.append(tmp)
    
    passed_day = days.pop(0)
    cnt = 1
    flag = False
    
    while days:
        next = days.pop(0)
        if next <= passed_day:
            cnt += 1
        else:
            answer.append(cnt)
            passed_day = next
            cnt = 1
    
    answer.append(cnt)
    
    return answer
