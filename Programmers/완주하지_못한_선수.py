def solution(participant, completion):
    dict1 = {i : 0 for i in participant}
    dict2 = {j : 0 for j in completion}
    
    for i in participant:
        dict1[i] += 1
    
    for j in completion:
        dict2[j] += 1
    
    for key in dict1.keys():
        if key in dict2.keys():
            if dict1[key] != dict2[key]:
                print("1")
                return key
        else:
            print("2")
            return key

    return answer
