import sys


def get_user_input():
    user_input = input("Please enter a list of integers separated by a comma. No spaces.\n")
    user_input_list = user_input.split(",")
    user_int_list = []

    for element in user_input_list:
        if element.isdigit():
            int_element = int(element)
            user_int_list.append(int_element)
        else:
            print("Sorry, one or many values that you entered are not integers. Please try again")
            sys.exit()

    return user_int_list


def switch(num, arr):
    arr[num + 1] = arr[num] + arr[num + 1]
    arr[num] = arr[num + 1] - arr[num]
    arr[num + 1] = arr[num + 1] - arr[num]
    return arr


def sorting(arr):
    size_arr = len(arr) - 1
    while size_arr > 0:
        for index in range(0, size_arr):
            if index < size_arr:
                if arr[index] > arr[index + 1]:
                    switch(index, arr)
        size_arr -= 1

    return arr


# --------------------------------------------------- running the sorting
user_list = get_user_input()
sorting(user_list)
print(f"This is your sorted list :\n{user_list}")
