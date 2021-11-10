def solution(n):
    answer = 0
    
    for i in range(n):

        print(n//(i+1))


        if n % (i+1) == 0:

            answer += i+1

    
    return answer


print(solution(12))