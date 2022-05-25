def solution(clothes):
    dict1 = {}
    for i in clothes:
        if i[1] in dict1.keys():
            dict1[i[1]] += 1
        else: 
            dict1[i[1]] = 1
        
    answer1 = 1
    for key in dict1.keys():
         answer1 *= dict1[key] + 1
            
    print(answer1)
    
    return answer1 -1
