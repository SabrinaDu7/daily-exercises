# https://www.techiedelight.com/coin-change-problem-find-total-number-ways-get-denomination-coins/
import sys
import numpy as np


def get_user_input():
    user_input_list = input("Please enter a list of integers separated by a comma. No spaces.\n").split(", ")
    user_int_list = []

    for element in user_input_list:
        if element.isdigit():
            int_element = int(element)
            user_int_list.append(int_element)
        else:
            print("Sorry, one or many values that you entered are not integers. Please try again")
            sys.exit()

    user_int_list.sort()
    return user_int_list


def generate_max_fits_list(target, lst):
    max_fits_list = []
    for index1 in range(0, len(lst)):
        temp_fit_lst = []
        max_fit = int(target/lst[index1])
        for index2 in range(0, max_fit + 1):
            temp_fit_lst.append(index2)
        max_fits_list.append(temp_fit_lst)
    return max_fits_list


def max_fit_combinations(arrays, out=None):
    # https://stackoverflows.co/questions/1208118/using-numpy-to-build-an-array-of-all-combinations-of-two-arrays
    arrays = [np.asarray(x) for x in arrays]
    dtype = arrays[0].dtype

    n = np.prod([x.size for x in arrays])
    if out is None:
        out = np.zeros([n, len(arrays)], dtype=dtype)

    # m = n / arrays[0].size
    m = int(n / arrays[0].size)
    out[:, 0] = np.repeat(arrays[0], m)
    if arrays[1:]:
        max_fit_combinations(arrays[1:], out=out[0:m, 1:])
        for j in range(1, arrays[0].size):
            # for j in xrange(1, arrays[0].size):
            out[j * m:(j + 1) * m, 1:] = out[0:m, 1:]
            # for i in range(0, len(out[j * m:(j + 1) * m])):
            # print(f"this is out[long] {out[j * m:(j + 1) * m][i]}")
    return out


def find_all_fit_ways(target, user_lst, fit_lst):
    target_fit_arr = np.array([], dtype='int32')
    arr = np.array(user_lst)
    arr.reshape((len(arr), 1))
    fit_arr = np.array(fit_lst)

    for i in range(0, len(fit_arr)):
        temp_sum = int(np.matmul(fit_arr[i], arr))
        if temp_sum == target:
            target_fit_arr = np.append(target_fit_arr, fit_arr[i])

    rows = int(len(target_fit_arr)/len(user_lst))
    cols = len(user_lst)
    target_fit_arr = target_fit_arr.reshape((rows, cols))
    return target_fit_arr


def find_coin_ways(fit_arr, user_lst):
    final_coin_lst = []
    fit_lst = fit_arr.tolist()
    for index in range(0, len(fit_lst)):
        temp_lst = []
        for count in range(0, len(user_lst)):
            if len(temp_lst) == 0:
                temp_lst = [user_lst[count]] * fit_lst[index][count]
            else:
                temp_lst = temp_lst + [user_lst[count]] * fit_lst[index][count]
        final_coin_lst.append(temp_lst)

    return final_coin_lst


user_target = int(input("Please insert a target sum.\n"))
user_input_lst = get_user_input()
max_fits = generate_max_fits_list(user_target, user_input_lst)
all_max_fit_combinations = max_fit_combinations(max_fits)
fit_array = find_all_fit_ways(user_target, user_input_lst, all_max_fit_combinations)
result = find_coin_ways(fit_array, user_input_lst)
print(f"The total number of ways is {len(result)}.\n{result}")
