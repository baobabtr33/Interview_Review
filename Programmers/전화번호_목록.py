def solution(phone_book):
    dict1 = {i : 0 for i in phone_book}
    phone_len = [len(i) for i in phone_book]
    phone_len = list(set(phone_len))
    phone_len.sort()
    
    for i in phone_book:
        for j in phone_len:
            if j < len(i):
                if i[0:j] in dict1.keys():
                    return False
            else:
                break
    
    return True
