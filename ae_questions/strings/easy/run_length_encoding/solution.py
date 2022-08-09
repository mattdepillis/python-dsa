"""
Write a function that takes a string and and returns its run-length encoding. Run-length encoding is a form of lossless data compression in which runs (or streaks) of data are stored in a single value and count. Runs of 10+ should be split into multiple runs.
"""
def run_length_encoding(string):
  encoding, char, count = "", string[0], 1
  for i in range(1, len(string)):
    if string[i] == string[i - 1]:
      if count == 9:
        encoding += f"{count}{char}"
        count = 0
      count += 1
    if string[i] != string[i - 1] or i == len(string) - 1:
      encoding += f"{count}{char}"
      char, count = string[i], 1

  return encoding

if __name__ == "__main__":
  print(run_length_encoding('AAAAAAAAAAbb""""3333333'))