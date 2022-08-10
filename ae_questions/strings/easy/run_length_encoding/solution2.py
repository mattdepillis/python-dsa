"""
Write a function that takes a string and and returns its run-length encoding. Run-length encoding is a form of lossless data compression in which runs (or streaks) of data are stored in a single value and count. Runs of 10+ should be split into multiple runs.
"""
def run_length_encoding(string):
  encoding = ""
  current = [string[0]]
  for i in string[1:]:
    if current[-1] == i and len(current) < 9:
      current.append(i)
    else:
      encoding += f"{len(current)}{current[0]}"
      current = [i]
  encoding += f"{len(current)}{current[0]}"
  return encoding

if __name__ == "__main__":
  # print(run_length_encoding('AAAAAAAAAAbb""""3333333'))
  # print(run_length_encoding('AAAAAAAAAAAAABBCCCCDD')) # 9A4A2B4C
  print(run_length_encoding('aA'))
  print(run_length_encoding(' '))