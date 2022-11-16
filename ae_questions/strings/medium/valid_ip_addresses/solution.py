"""
Given a string of length <= 12, write a function that returns all the possible IP addresses that can be created be inserting 3 "."s into the string. Reminder: the integers (each 1-3 digit num separated by the .) in the IP address must be from 0-255.

TC: O(1) ???
SC: O(1) ??? 
-- This probably has to do with the fact that valid IP address length is bounded from 4-12.
"""
# determines whether a digit combo is valid.
def is_valid(string):
  if len(string) > 1 and string[0] == "0":
    return False
  return int(string) < 256

# loops through to find valid combinations of digits.
# when 3 previous iterations have completed, checks to see whether the current result is valid.
def find_valid(string, shift, iterations, list, combo):
  for i in range(shift + 1, shift + 4):
    if i > len(string): return
    if is_valid(string[shift:i]):
      if iterations < 3 and len(combo) <= 3:
        find_valid(string, i, iterations + 1, list, combo + [string[shift:i]])
      else:
        c = combo + [string[shift:i]]
        if ''.join(c) == string:
          list.append('.'.join(c))
  return list

# base setup function
def valid_ip_addresses(string):
  return find_valid(string, shift=0, iterations=0, list=[], combo=[]) or []


if __name__ == "__main__":
  print(valid_ip_addresses("1921680")) # ["1.9.216.80", "1.92.16.80", "1.92.168.0", "19.2.16.80", "19.2.168.0", "19.21.6.80", "19.21.68.0", "19.216.8.0", "192.1.6.80", "192.1.68.0", "192.16.8.0"]

  print(valid_ip_addresses("11")) # []