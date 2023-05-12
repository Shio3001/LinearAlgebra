import numpy as np
import copy

# user_column = int(input())
user_row = int(input())

target_array = []
ans_target_array = []


for i in range(user_row):
    input_temp_target_array = list(map(int, input().split()))

    target_array.append(input_temp_target_array)

ans_target_array = np.array(target_array)

kai_list = [1] * (len(ans_target_array))

print("ans" , ans_target_array)

for ni in range(user_row): #現在の行 #ホウキとなる行
    for ti in range(ni + 1,user_row): #対象 #ホウキの餌食となる行

        # print(ni,ti)
        
        # print("a",this_ni_row , this_ti_row)

        common_n = ans_target_array[ni][ni] 
        common_t = ans_target_array[ti][ni] 

        print("common",common_n,common_t,target_array[ni],target_array[ti])

        this_ni_row = ans_target_array[ni] * common_t
        this_ti_row = ans_target_array[ti] * common_n * -1

        print("b",this_ni_row , this_ti_row)

        ans_target_array[ti] = this_ni_row + this_ti_row

        print(common_n , common_t)

        # print(target_array)

print("ans" , ans_target_array)

# print(target_array)

ans2_target_array = np.array(ans_target_array)
#代入して行って、それぞれの変数の値を求める

for ph in range(user_row):
    ph_row = user_row - ph - 1

    right = ans_target_array[ph_row][-1]
    now_coefficient = right / ans_target_array[ph_row][ph_row]

    kai_list[ph_row] = now_coefficient

    for i in range(ph_row):
        ans2_target_array[i][-1] -= ans_target_array[i][ph_row] * now_coefficient

print("ans" , ans2_target_array)


print(kai_list)