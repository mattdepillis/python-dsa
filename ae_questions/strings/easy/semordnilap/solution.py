"""
Write a function that takes a list of unique strings and returns a list of the semordnilap pairs. A semordnilap pair is a pair of strings for which both strings are the reverse of the other.

TC: O(m * n) -- where m = length of the array n = length of the longest word (must reverse words)
SC: O(m * n) -- where m = length of the array n = length of the longest word (worst-case must store every word, and max storage per word == len(longest_word))
"""
def semordnilap_pairs(array):
  pairs, store = [], set()
  for word in array:
    reverse = word[::-1]
    if reverse in store:
      pairs += [[reverse, word]]
    store.add(word)
  return pairs


if __name__ == "__main__":
  print(semordnilap_pairs(
    ["liver", "dog", "hello", "desserts", "evil", "test", "god", "stressed", "racecar", "palindromes", "semordnilap", "abcd", "live"]
  ))