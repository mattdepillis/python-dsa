"""
Given a row of seats in a theater in which the end seats are always taken, determine the best seat (the one with the most space surrounding it) to sit in. Space is denoted by 0s.
Notes:
- if there are equally-optimal seats, choose the one closest to the left.
- if you can't find a seat, return -1.

TC: O(n) -- one-pass solution
SC: O(1) -- consistent variable assignment for any n values
"""

def best_seats(array):
  last_taken = most_consecutive = 0
  best_seat = None

  for i in range(last_taken, len(array)):
    if array[i] != 0:
      if array[i - 1] == 0 and i - last_taken > most_consecutive:
        most_consecutive = i - last_taken
        best_seat = last_taken + (i - last_taken) // 2
      last_taken = i

  return -1 if best_seat is None else best_seat


if __name__ == "__main__":
  print(best_seats(
    [1, 0, 1, 0, 0, 0, 1]
    # [1]
  ))

  print(best_seats(
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
  ))