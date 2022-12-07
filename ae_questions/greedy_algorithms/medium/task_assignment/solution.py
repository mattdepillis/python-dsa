"""
Given an integer k representing the number of workers and an array of 2k tasks to accomplish, write a function that gets the tasks done in the optimal amount of time. Tasks are done in parallel. The function should return a list of pairs that represent the indices of the tasks from the input task list that each worker will do.
"""
def task_assignment(k, tasks):
  assignments = []

  for i in range(len(tasks)):
    tasks[i] = {'index': i, 'value': tasks[i]}

  t = sorted(tasks, key=lambda x: x['value'])

  for i in range(k):
    assignments.append([ t[i]['index'], t[len(t) - 1 - i]['index'] ])

  return assignments


if __name__ == "__main__":
  print(task_assignment(3, [1, 3, 5, 3, 1, 4]))