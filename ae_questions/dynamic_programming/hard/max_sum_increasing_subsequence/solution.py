"""
Write a function that takes a list of integers and returns the greatest sum that can be generated from a subsequence of the array consisting of strictly increasing values.
"""
# def max_sum_increasing_subsequence(array):
#   max_subsequence = [float('-inf'), []]

#   for i in range(len(array)):
#     # print('*****************\n array[i]', array[i], '\n*************')
#     subseq = [array[i]]
#     for j in reversed(range(0, i)):
#       # print('array[j]', array[j])
#       if array[j] < subseq[0] and array[j] > 0:
#         subseq.insert(0, array[j])
#       elif array[j] > subseq[0]:
#         if array[j] >= array[i]: continue
#         smaller_sum = k = 0
#         while k < len(subseq):
#           if array[j] >= subseq[k]:
#             smaller_sum += subseq[k]
#             k += 1
#           else: break
#         # print(f"smaller_sum: {smaller_sum}, array[i]: {array[i]}, array[j]: {array[j]}, subseq[k]: {subseq[k]}")
#         if smaller_sum > array[j]: continue
#         else:
#           # print('sbefore', subseq)
#           subseq = [array[j]] + subseq[k:]
#       # print('subseq', subseq)

#     if sum(subseq) > max_subsequence[0]: max_subsequence = [sum(subseq), subseq]

#   return max_subsequence

if __name__ == "__main__":
  print(max_sum_increasing_subsequence([10, 70, 20, 30, 50, 11, 30])) # [110, [10, 20, 30, 50]]
  print(max_sum_increasing_subsequence([-1, 1]))
  print(max_sum_increasing_subsequence([8, 12, 2, 3, 15, 5, 7]))
  print(max_sum_increasing_subsequence([10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]))