"""
Imagine a set of cities laid out in a circle, connected by one road. Given an array of distances between those cities, the number of gallons of gas you can get in each city, and the MPG a car gets, calculate the city you should start in to travel around the circle of cities ending with no gas left in the tank. There is exactly one starting city that is valid for a given array of distances.

TC: O(n)
SC: O(1)
"""
def valid_starting_city(distances, gallons, mpg):
  diff = valid_city = diff_at_valid_city = 0
  gallons = [i * mpg for i in gallons]

  # NOTE: will always be the city AFTER the one where diff is largest
  for i in range(1, len(distances)):
    diff += gallons[i - 1] - distances[i - 1]
    if diff < diff_at_valid_city:
      valid_city, diff_at_valid_city = i, diff

  return valid_city

if __name__ == "__main__":
  # print(valid_starting_city([5, 25, 15, 10, 15], [1, 2, 1, 0, 3], 10))
  print(valid_starting_city([15, 20, 25, 30, 35, 5], [0, 3, 0, 0, 1, 1], 26))