import sys

# condition 1: check if start point coordinates == endpoint coordinates
# condition 2: check if the tile start point is moving to goes off the board/ passes the edge
# condition 3: check if the tile start point is moving to is False
# condition 4: check if the tile start point is moving to has been passed through by previous start points.


def hardcoded_board():
    # arr[row][col]
    # arr[row]

    arr = [[True, True, True, True],
           [True, True, False, True],
           [True, True, True, False],
           [False, True, True, True],
           [True, True, False, True],
           [True, False, False, True]]

    for row in arr:
        print(row)

    return arr


def went_same_coordinates_already(current_coordinates):
    if len(coordinates_list) == 0:
        return False
    elif current_coordinates in coordinates_list:
        return True
    else:
        return False


def get_user_coordinates(board):
    user_input_coordinates = input("\nPlease insert your start coordinates, followed by your end coordinates as such"
                                   ": row, column, row, column.\n").split(", ")
    if user_input_coordinates[0].isdigit() and user_input_coordinates[1].isdigit():
        array = [int(i) for i in user_input_coordinates]
        if array[0] < 0 or array[0] > (len(board) - 1) or array[1] < 0 or array[1] > (len(board[0]) - 1):
            print("These coordinates are not part of the board.")
            sys.exit()
        return array

    else:
        print("Some or all of the elements in your list is/aren't numbers. I can't sort this list for you.")
        sys.exit()


my_board = hardcoded_board()
user_coordinates = get_user_coordinates(my_board)
start_row_init = user_coordinates[0]
start_col_init = user_coordinates[1]
end_row_user = user_coordinates[2]
end_col_user = user_coordinates[3]
coordinates_list = []
num_steps_list = []
final_coordinates_path = []


def find_paths(start_row, start_col, end_row, end_col, array):
    global final_coordinates_path
    if not array[start_row][start_col]:
        print("Sorry, you can't start on a 'False' tile.")
        sys.exit()

    if start_row == end_row and start_col == end_col:  # condition 1
        if len(num_steps_list) != 0:
            if num_steps_list[0] > len(coordinates_list):
                num_steps_list.pop(0)
                num_steps_list.append(len(coordinates_list))
                final_coordinates_path = coordinates_list.copy()
        else:
            num_steps_list.append(len(coordinates_list))
        coordinates_list.pop(-1)
        return

    if start_col != 0 and array[start_row][start_col - 1]:
        if went_same_coordinates_already([start_row, start_col - 1]) is False:  # if start point can move left
            coordinates_list.append([start_row, start_col])
            find_paths(start_row, start_col - 1, end_row, end_col, array)

    if start_row != 0 and array[start_row - 1][start_col]:
        if went_same_coordinates_already([start_row - 1, start_col]) is False:  # if start point can move up
            coordinates_list.append([start_row, start_col])
            find_paths(start_row - 1, start_col, end_row, end_col, array)

    if start_col != (len(array[0]) - 1) and array[start_row][start_col + 1]:  # if start point can move right
        if went_same_coordinates_already([start_row, start_col + 1]) is False:
            coordinates_list.append([start_row, start_col])
            find_paths(start_row, start_col + 1, end_row, end_col, array)

    if start_row != (len(array) - 1) and array[start_row + 1][start_col]:
        if went_same_coordinates_already([start_row + 1, start_col]) is False:  # if start point can move down
            coordinates_list.append([start_row, start_col])
            find_paths(start_row + 1, start_col, end_row, end_col, array)

    if start_row == start_row_init and start_col == start_col_init:
        if len(num_steps_list) == 0:
            print("Null")
        else:
            print(f"The minimum steps to get to ({end_row}, {end_col}) from ({start_row}, {start_col}) is "
                  f"{num_steps_list[-1]}. \nYou must follow the following path : {final_coordinates_path}.")
    else:
        coordinates_list.pop(-1)
        return


# -------------------------------------------------------------------------------------------------------------------------
find_paths(start_row_init, start_col_init, end_row_user, end_col_user, my_board)
