

# if num % 5 != 0 and num % 3 != 0:
#     result = -1

# elif num % 3 == 0 and num % 5 == 0:
#     result = num // 5

# elif num

# else:
#     res_5 = num // 5
#     res_3 = num % 5 // 3

num = int(input())

result = 0

arr_3 = []
arr_5 = []
result_arr = []

for i in range(int(num/3)):
    arr_3.append(i+1)
for i in range(int(num/5)):
    arr_5.append(i+1)

for i in range(len(arr_3)):
    for j in range(len(arr_5)):
        if arr_3[i]*3 + arr_5[j]*5 == num:
            result_arr.append(arr_3[i]+arr_5[j])
        elif arr_3[i] * 3 == num:
            result_arr.append(arr_3[i])
        elif arr_5[j] * 5 == num:
            result_arr.append(arr_5[j])


print(min(result_arr))
