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
  min_indices, rewards = [0], [1 for _ in range(len(array))]
  for i in range(1, len(array)):
    if array[i] < array[i - 1]:
      if len(min_indices) and min_indices[-1] == i - 1:
        min_indices[-1] = i
      else: min_indices.append(i) 

  prev, to_increase = 0, []
  for i in range(len(rewards)):
    if len(min_indices) > 1 and i == min_indices[1]:
      for idx in reversed(to_increase):
        rewards[idx] = rewards[idx + 1] + 1
      to_increase = []
      min_indices.pop(0)
    closer_min = abs(min_indices[0] - i) if len(min_indices) < 2 else min(abs(min_indices[0] - i), abs(min_indices[1] - i))
    to_add = closer_min

    if i > 0:
      if array[i] > array[i - 1] and closer_min <= prev:
        to_add = prev
      if array[i] < array[i - 1] and closer_min >= prev:
        print('hit')
        if not len(to_increase): to_increase.append(i - 1)
        to_increase.append(i)

    print(f"closer_min: {closer_min}, i: {i}, array[i]: {array[i]}, prev: {prev}, reward: {to_add + 1}")
    rewards[i] += to_add
    prev = rewards[i]

  print(array)
  # print('\n')
  print(rewards)
  # print('\n')
  return sum(rewards)
  

if __name__ == "__main__":
  # print(min_rewards([8, 4, 2, 1, 3, 6, 7, 9, 5])) # 25
  # print(min_rewards([10, 5])) # 3
  # print(min_rewards([5, 10])) # 3
  # print(min_rewards([800, 400, 20, 10, 30, 61, 70, 90, 17, 21, 22, 13, 12, 11, 8, 4, 2, 1, 3, 6, 7, 9, 0, 68, 55, 67, 57, 60, 51, 661, 50, 65, 53])) # 93
  print(min_rewards([0, 4, 2, 1, 3]))

  """
  1 -> 2 -> 1 -> 2 -> 1 -> 2 -> 1 -> 2 -> 1, -> 2 -> 1 -- 16
  2 -> 1 -> 
  """