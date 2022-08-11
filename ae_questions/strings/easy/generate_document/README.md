---
Problem: Generate Document
Type: String
Date Written: 08-10-2022
---

# Problem
Given a string of available characters to use (case sensitive + special characters), and a string (document) you want to generate from the available characters, write a function that returns a boolean indicating whether or not you were able to do so.

For example, python```generate_document('aheaollabbhb', 'hello')``` should return ```True```.

# Solution
A dict is a very convenient data structure to use for this problem - it has constant-time insertion and access, making it a great choice as an intermediary data structure to create a ledger of which characters are at our disposal.

Using a dict, we can loop through the character list once to create that ledger. Then, we can loop through the document to determine whether or not every character is available in our ledger.

NOTE: I could have written one for-loop through the document that assesses whether or not a given char is in the characters string, and replaced it. I didn't do this. I could reassign the string to python```string.replace(char, val, num)``` but it seems a bit anti-pattern-ish. If I were to write a second solution to the problem, maybe I'd try this.

**Pseudocode:**
- initialize a dict that acts as a ledger for all available letters to use.
- loop through the characters string.
  - if the character isn't a key in the dict, add it and init its value to 0.
  - add 1 to ```char_dict[c]```.
- loop through the document string.
  - if the dict doesn't have a key for a character ```c```, or ```char_dict[c]``` is 0 (the balance has been withdrawn), return False.
  - else subtract 1 from the key's value in the ledger.
- return True if made through the second for-loop.

**Big O:**
- O(n + m) time, where n = len(characters) and m = len(document)
  - since we loop through both strings, and all operations inside the for-loops are time-constant, worst-case time is O(n + m).
- O(c) space, where c = # of unique characters in characters string
  - we need to store c keys and values in the ledger.