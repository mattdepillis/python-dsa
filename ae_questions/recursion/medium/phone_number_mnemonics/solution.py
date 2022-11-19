"""
Digits on a phone keypad have associations to different letters of the alphabet, forming mnemonics. Using the provided digit-letter guide, return all possible mnemonics for a given phone number.

TC: O(4^n * n) -- the maximum number of recursive calls the algorithm will make is 4^n (4 = max chars assigned to one digit, n coming from the amount of times we need to recurse to get the final string for each combo). Multiply by n because creating the string at each recursive stop is an O(n) time operation.

SC: O(4^n * n) -- maximum number of mnemonic combinations for len(string) = n is 4^n, and each of those strings requires space for n characters.
"""

# mnemonics mapping for the problem
mapping = {
  "0": ["0"],
  "1": ["1"],
  "2": ["a", "b", "c"],
  "3": ["d", "e", "f"],
  "4": ["g", "h", "i"],
  "5": ["j", "k", "l"],
  "6": ["m", "n", "o"],
  "7": ["p", "q", "r", "s"],
  "8": ["t", "u", "v"],
  "9": ["w", "x", "y", "z"]
}

# helper recursor function
def pn_recursor(i, string, set, m):
  if i >= len(set):
    if string not in m:
      m.append(string)
    return
  
  for item in set[i]:
    s = string + item
    pn_recursor(i + 1, s, set, m)
  
  return m

# staging function
def phone_number_mnemonics(number):
  return pn_recursor(0, "", set=[mapping[digit] for digit in number], m=[])


if __name__ == "__main__":
  print(phone_number_mnemonics("1905"))