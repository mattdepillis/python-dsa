"""
Imagine a set of cities laid out in a circle, connected by one road. Given an array of distances between those cities, the number of gallons of gas you can get in each city, and the MPG a car gets, calculate the city you should start in to travel around the circle of cities ending with no gas left in the tank. There is exactly one starting city that is valid for a given array of distances.
"""
def valid_starting_city(distances, gallons, mpg):
  diff = 0
  for i in range(len(gallons)):
    gallons[i] *= mpg
    city_diff = gallons[i] - distances[i]
    if diff < 0 and city_diff > 0: return i
    diff += city_diff
  return 0 if gallons[0] > 0 else len(gallons) - 1

if __name__ == "__main__":
  # print(valid_starting_city([5, 25, 15, 10, 15], [1, 2, 1, 0, 3], 10))
  print(valid_starting_city([15, 20, 25, 30, 35, 5], [0, 3, 0, 0, 1, 1], 26))