# https://www.techiedelight.com/find-pair-with-given-sum-array/
import sys
import numpy as np


def get_user_input():
    user_input = input("Please enter a list of integers separated by a comma. No spaces.\n")
    user_input_list = user_input.split(", ")
    user_int_list = np.array([], dtype='int32')

    for element in user_input_list:
        if element.isdigit():
            user_int_list = np.append(user_int_list, int(element))
        else:
            print("Sorry, one or many values that you entered are not integers. Please try again")
    return user_int_list


def find_sum_pair(target, arr):
    start_index = 0
    size_arr = len(arr) - 1
    sum_pair_list = np.empty(shape=(0, 2), dtype='int32')
    while start_index < size_arr:
        for end_index in range(start_index, size_arr):
            if start_index != end_index:
                if arr[start_index] + arr[end_index] == target:
                    sum_pair_list = np.append(sum_pair_list, np.array([[arr[start_index], arr[end_index]]]), axis=0)
        start_index += 1
    if len(sum_pair_list) == 0:
        print("No pair")
        sys.exit()
    else:
        return sum_pair_list


def printing(array):
    index = 0
    indiv_sum_pairs = np.split(sum_pair_2D_array, array.ndim, axis=0)
    while index <= array.ndim - 1:
        print(f"Pair found: {indiv_sum_pairs[index]}")
        index += 1


goal = input("Please insert a target sum. \n")
user_list = get_user_input()
sum_pair_2D_array = find_sum_pair(int(goal), user_list)
printing(sum_pair_2D_array)
