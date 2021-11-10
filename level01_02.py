def solution(numbers):
    answer = -1

    sum = 0

    for i in range(len(numbers)):
        sum += numbers[i]     


    answer = 45-sum
    return answer


numbers = [1,2,3,4,5,6,7,8,0]

print(sum(numbers))

print(solution(numbers))

# sum(배열) 배열 합