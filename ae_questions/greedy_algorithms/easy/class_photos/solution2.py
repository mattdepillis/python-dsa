"""
Given 2 arrays, one of kids standing in front of a class photo, and one of kids in the back, determine whether or not a class photo can be taken. Rules: all "students" in the back row must be taller than the student standing directly in front of them.
NOTE: TLDR - initial order doesn't matter in a given array. For example, array1 of [1, 2, 3] and array2 of [3, 2, 4] should return true as array2 can be arranged such that each kid in the back higher than in the front. 
"""

"""
TC: O(nlog(n)) - due to array sort. nlog(n) + nlog(n) + n -> nlog(n) complexity
SC: O(1) - because taller stores a string of 3 or 4 chars - irrespective of array size.
"""
def class_photo(red, blue):
  red.sort(), blue.sort()

  taller = 'red' if red[0] > blue[0] else 'blue'
  for i in range(len(red)):
    if (taller == 'red' and red[i] <= blue[i]) or (taller == 'blue' and blue[i] <= red[i]):
      return False

  return True

if __name__ == "__main__":
  print(class_photo([5, 8, 1, 3, 4], [6, 9, 2, 4, 3]))