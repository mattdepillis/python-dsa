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
  min_indices, rewards = [], [1 for _ in range(len(array))]
  for i in range(1, len(array)):
    if array[i] < array[i - 1]:
      if len(min_indices) and min_indices[-1] == i - 1:
        min_indices[-1] = i
      else: min_indices.append(i)

  for i in range(len(rewards)):
    rewards[i] += abs(min_indices[0] - i)
    if min_indices[0] == i and len(min_indices) > 1: min_indices.pop(0)

  print(rewards)
  return sum(rewards)
  

if __name__ == "__main__":
  print(min_rewards([8, 4, 2, 1, 3, 6, 7, 9, 5])) # 25
  print(min_rewards([10, 5])) # 3