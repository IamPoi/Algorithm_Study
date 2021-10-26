def solution(lottos, win_nums):
    answer = []
    
    cnt = 0
    zero = 0

    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt = cnt + 1
        if lottos[i] == 0:
            zero = zero + 1
            
    max = cnt + zero

    if max == 6:
        answer.append(1)
    elif max == 5:
        answer.append(2) 
    elif max == 4:
        answer.append(3)
    elif max == 3:
        answer.append(4) 
    elif max == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    if cnt == 6:
        answer.append(1)
    elif cnt == 5:
        answer.append(2) 
    elif cnt == 4:
        answer.append(3)
    elif cnt == 3:
        answer.append(4) 
    elif cnt == 2:
        answer.append(5)
    else:
        answer.append(6)

    return answer