"""
Calculate the min or max combined speed of pairings of tandem bikes (a tandem is comprised of one "rider" from each list). A bike's speed is the max of the two riders on the bike. If fastest=true, return the maximum possible combined speed; else return the min.
"""
def tandem_bicycle(red, blue, fastest):
  if fastest:
    combined = sorted(red + blue, reverse=fastest)
    return sum(combined[:len(red)])
  red.sort(), blue.sort()
  speed = 0
  for i in range(len(red)):
    speed += max(red[i], blue[i])
  return speed


if __name__ == "__main__":
  # print(tandem_bicycle([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], True))
  print(tandem_bicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], False))
  # print(tandem_bicycle())