idef solution(bridge_length, weight, truck_weights):
    answer = 0
    
    on_bridge = 0
    on_truck = []
    next_truck = 0
    while truck_weights or on_truck:
        flag = False
        for truck in on_truck:
            truck[1] -= 1
            if truck[1] == 0:
                on_bridge -= truck[0]
                flag = True
                
        if flag: del on_truck[0]
            
        if truck_weights:
            if  on_bridge + truck_weights[0] <= weight:
                next_truck = truck_weights.pop(0)
                on_bridge += next_truck 
                on_truck.append([next_truck,bridge_length])
            
        answer += 1

    return answer
