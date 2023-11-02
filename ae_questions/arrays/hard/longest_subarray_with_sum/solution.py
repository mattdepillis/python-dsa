"""

"""
def longest_subarray_with_sum(array, target):
    longest_subarray = []
    anchor, total_sum = -1, 0

    for i in range(len(array)):
        total_sum += array[i]
        sum_at_anchor = 0 if anchor == -1 else array[anchor]

        if total_sum - sum_at_anchor == target or array[i] == target:
            if array[i] == target or anchor == -1 or i - anchor > longest_subarray[1] - longest_subarray[0]:
                longest_subarray = [anchor + 1, i]
        elif total_sum - sum_at_anchor > target: anchor += 1
        array[i] = total_sum

    return longest_subarray


if __name__ == "__main__":
    # print(longest_subarray_with_sum(
    #     [1, 2, 3, 4, 3, 3, 1, 2, 1],
    #     10
    # )) # [4, 8]

    print(longest_subarray_with_sum(
        [1, 4, 10, 15, 31, 7, 1, 40, 0, 20, 1, 1, 1, 1, 2, 1],
        0
    ))