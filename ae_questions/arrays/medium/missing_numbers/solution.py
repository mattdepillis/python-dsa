"""

"""
def missing_numbers(nums):
  for _ in range(2): nums.append(None)
  sorted_to = 0
  for _ in range(len(nums)):
    i = sorted_to

    while i < len(nums) - 1:
      if nums[i] is not None and nums[i] != i + 1:
        sorted_to = i
        break
      i += 1

    if nums[i] is None: continue
    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
  return nums


if __name__ == "__main__":
  # print(missing_numbers(
  #   [1, 15, 16, 17, 18, 19, 20, 21, 22, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  # )) # 1, 2

  print(missing_numbers(
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  ))