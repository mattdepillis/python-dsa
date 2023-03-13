"""
Given a list of scores representing how well each student in the class did on an assignment, return the minimum total rewards required to be handed out.

Rules:
- each student must get at least reward = 1
- a student must receive strictly more rewards than a student with a lower score next to him/her in the scores array
- a student must receive strictly fewer rewards than a student with a higher score next to him/her in the scores array

TC: O(n) - must iterate through n elements 3 separate times:
  - get min_indices
  - set rewards values
  - sum the rewards
SC: O(n) - new rewards array of size n
"""
def min_rewards(array):
  rewards = [1 for _ in array]
  for i in range(1, len(array)):
    if array[i] > array[i - 1]: rewards[i] = rewards[i - 1] + 1
  for i in reversed(range(len(array) - 1)):
    if array[i] > array[i + 1]:
      rewards[i] = max(rewards[i], rewards[i + 1] + 1)
  return sum(rewards)
  

if __name__ == "__main__":
  # print(min_rewards([8, 4, 2, 1, 3, 6, 7, 9, 5])) # 25
  # print(min_rewards([10, 5])) # 3
  # print(min_rewards([5, 10])) # 3
  print(min_rewards([800, 400, 20, 10, 30, 61, 70, 90, 17, 21, 22, 13, 12, 11, 8, 4, 2, 1, 3, 6, 7, 9, 0, 68, 55, 67, 57, 60, 51, 661, 50, 65, 53])) # 93
  # print(min_rewards([0, 4, 2, 1, 3]))