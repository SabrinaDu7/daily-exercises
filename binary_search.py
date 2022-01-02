import bubble_sort as bs


# ------------------------------------------------------------------------------- functions
def locate_and_compare_to_midpoint(num, arr):
    start = 0
    end = len(arr) - 1

    while (end - start) != 1:
        mid = int((start + end)/2)
        if num < arr[mid]:
            end = mid
        elif num == arr[mid]:
            return mid
        else:
            start = mid
    if num >= arr[end]:
        return end + 1
    elif num <= arr[start]:
        return start - 1
    else:
        return end


def user_num():
    user_input = input("\nPlease enter a number to be inserted into the array.\n")
    if user_input.isdigit():
        user_input = int(user_input)
        return user_input
    else:
        print("Please try again and enter a valid integer.")
        return False


# ------------------------------------------------------------------------------- executing the search and insert
user_input_num = user_num()
insert_index = locate_and_compare_to_midpoint(user_input_num, bs.user_list)
final_arr = bs.user_list
final_arr.insert(insert_index, user_input_num)
print(f"This is your new sorted list: \n{final_arr}")
