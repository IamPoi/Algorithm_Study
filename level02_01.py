def solution(str1, str2):
    answer = 0

    str1 = str1.upper()
    str2 = str2.upper()

    str1_arr = []
    str2_arr = []

    for i in range(len(str1)):
        if i+1 == len(str1):
            break
        if str1[i] != " " and str1[i+1] != " " and str1[i].isalpha() == True and str1[i+1].isalpha() == True:
            str1_arr.append(str1[i] + str1[i+1])

    for i in range(len(str2)):
        if i+1 == len(str2):
            break
        if str2[i] != " " and str2[i+1] != " " and str2[i].isalpha() == True and str2[i+1].isalpha() == True:
            str2_arr.append(str2[i] + str2[i+1])

    print(str1_arr)
    print(str2_arr)

    union = 0
    intersection = 0

    for i in range(len(str1_arr)):
        for j in range(len(str2_arr)):
            if str1_arr[i] == str2_arr[j]:
                intersection += 1


    union = list(set(str1_arr + str2_arr))

    if len(union) != 0:
        answer = int(intersection / len(union) * 65536)
    else:
        answer = 65536
    
    return answer

print(solution("aa1+aa2","AAAA12"))