# write solution explanation here
def two_number_sum(array, target_sum):
  for i in range(len(array)):
    arr_to_search = array[i:]
    if len(arr_to_search) < 2:
      return []
    for j in range(1, len(arr_to_search)):
      if arr_to_search[0] + arr_to_search[j] == target_sum:
        return [arr_to_search[0], arr_to_search[j]]
    

if __name__ == "__main__":
  print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
  print(two_number_sum([4, 6], 10))
  print(two_number_sum([4, 6, 1], 5))
  print(two_number_sum([14], 15))
  print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 15))