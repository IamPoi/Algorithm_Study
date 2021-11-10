def solution(year):
    answer = 0

    if year % 400 ==0:
        answer = 1
    elif year % 4 ==0 and year % 100 != 0:
        answer = 1

    return answer

print(solution(2000))

year = int(input())

answer = 0

if year % 400 ==0:
    answer = 1
elif year % 4 ==0 and year % 100 != 0:
    answer = 1

print(answer)