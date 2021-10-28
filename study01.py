# def solution(L, x):
#     answer = 0
    
#     L.sort()
    
#     while(True):
#         if((L[len(L)//2)-1] < x):
#             L = L[:(len(L)//2) - 1]
        
#         elif(L[(len(L)//2) - 1] > x):
#             L = L[ (len(L)//2) - 1 :]
        
#         if(L[0] == x):
#             break
#     answer = L[0]
    
    
#     return answer

def solution(L, x):
    answer = 0

    upper = len(L) - 1 
    low = 0

    L.sort()
    while(True):
        if(L[len(L)//2 -1] > x):
            L = L[:L[len(L)//2 -1]]
            upper = L[len(L)//2 -1]
        elif L[len(L)//2 -1] < x:
            L = L[L[len(L)//2 -1]:]
            low = L[len(L)//2 -1]
        

        if L[0] == x:
            break
        
    answer = (upper + low) // 2

    return answer


# L = [1,2,3,4,5,6,7,8,9,10]

# print(solution(L,9))


def solution(L, x):
    answer = 0

    lower = 0
    upper = len(L) -1 
    idx = -1

    # while lower <= upper
    for i in range(10):
        middle = (upper+lower) // 2

        print(upper)
        print(lower)
        print(middle)

        if L[middle] == x:
            answer = middle
            break
        elif L[middle] > x:
            upper = middle
        elif L[middle] < x:
            lower = middle
        elif lower == middle or upper == middle:
            answer = -1
            break
        

    return answer

L = [1,2,3,4,5,6,7,8,9,10]

print(solution(L,12))