"""
Given 2 strings s and t, determine whether t is an anagram of s.
"""

"""
Original solution.
"""
class Solution(object):
  def isAnagram(self, s, t):
    # right off the bat, if strings aren't of same length then return False
    if len(s) != len(t):
      return False

    # transform both strs into lists and sort them by char
    s = list(s)
    s.sort()

    t = list(t)
    t.sort()

    # if lists equal, return True
    if s == t:
      return True
    else:
      return False

if __name__ == "__main__":
  print(Solution().isAnagram('cat', 'tac'))