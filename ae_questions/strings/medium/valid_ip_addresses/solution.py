"""
Given a string of length <= 12, write a function that returns all the possible IP addresses that can be created be inserting 3 "."s into the string. Reminder: the integers (each 1-3 digit num separated by the .) in the IP address must be from 0-255.
"""
def is_valid(string):
  return int(string) < 256

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

def valid_ip_addresses(string):
  valid, combo = [], []
  iterations = shift = 0
  find_valid(string, shift, iterations, valid, combo)
  return valid


if __name__ == "__main__":
  print(valid_ip_addresses("1921680"))