"""

"""
def semordnilap_pairs(array):
  pairs, store = [], set()
  for word in array:
    reverse = word[::-1]
    if reverse in store:
      pairs += [[reverse, word]]
      store.remove(reverse)
    store.add(word)
  return pairs


if __name__ == "__main__":
  print(semordnilap_pairs(
    ["liver", "dog", "hello", "desserts", "evil", "test", "god", "stressed", "racecar", "palindromes", "semordnilap", "abcd", "live"]
  ))