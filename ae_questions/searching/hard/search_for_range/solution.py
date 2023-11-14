"""

"""
def check_subarray_middle(array, target, start, end, side):
    print(side, array[start:end + 1])
    middle = ((end - start) // 2) + start
    shift = array[middle] < target if side == "left" else array[middle] > target

    return shift, middle


def search_for_range(array, target):
    start, end = 0, len(array) - 1

    while start < end:
        middle = ((end - start) // 2) + start

        # print(f"start: {start}, end: {end}")

        # print("middle", middle)

        shift_start, left_middle = check_subarray_middle(array, target, start, middle, "left")
        shift_end, right_middle = check_subarray_middle(array, target, middle + 1, end, "right")

        if shift_start: start = left_middle + 1
        if shift_end: end = right_middle - 1

        if not shift_start and not shift_end: return [start, end]

    return [-1, -1]


if __name__ == "__main__":
    print(search_for_range(
        [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], target=45 # [4, 9]
    ))