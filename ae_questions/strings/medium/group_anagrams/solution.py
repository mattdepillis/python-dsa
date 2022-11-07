"""
Write a function that takes in a list of strings and groups anagrams together.

TC: O(w * n * log(n)), where w = # words, n = len(longest_word) -- this is because we need to split, sort and join each word
SC: O(wn) -- need to store wn bytes, where storage is proportional to the number of words provided + the max word length
"""
def group_anagrams(words):
  anagrams = {}
  for word in words:
    split = sorted([*word])
    sorted_word = "".join(split)
    if sorted_word not in anagrams.keys():
      anagrams[sorted_word] = [word]
    else:
      anagrams[sorted_word].append(word)

  return [value for value in anagrams.values()]


if __name__ == "__main__":
  print(group_anagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))