---
Problem: Tournament Winner
Type: Array
Date Written: 07-17-2022
---

# Problem
Write an algorithm that determines the winner of a tournament in which each team plays every other team exactly once. There will always be one definite winner. A win in a game adds 3 points to the team's total.
Two lists should be passed to the function:
- ```matchups```, which contains nested lists of length 2: [home_team, away_team]
- ```results```, which is a list of the results from the games. results[0] corresponds to the result of the first game. 1 means the home_team won; 0 means the away_team won.

Return the name of the winning team.

For example, python```tournament_winner([['Eagles', 'Cowboys'], ['Dolphins', 'Eagles'], ['Cowboys', 'Dolphins']], [1, 0, 0])))``` should return ```Eagles```.

# Solution
My initial solution makes use of Python's dict data structure. I loop over each result in the results array and determine which team in the matchups array won that given game. If the winner exists in the scores dict, I increment its point total by 3. Else, I add it to the dict and set its total to 3. Then, I find the key with the highest point total and return it.

**Pseudocode:**
- create a dict ```points``` to store the winner point totals.
- loop through the results array.
- for each result,
  - determine the winner. Home team is 1, away team is 0.
  - if the winner exists in ```points```, increment its total by 3.
  - else, create the key and set its value to 3.
- return the team with the max points after looping through by determining which key has the highest value. python```max(points, key=points.get)``` returns the key with the highest total in value. Simply returning python```max(points)``` would return the highest-valued key by first letter, and python```max(points.values)``` would return the highest point total as an int. To return the key with the highest value, we must search by setting key equal to python```points.get``` -- python```points.get``` fetches the highest value, and then python```key=``` returns the corresponding key.

**Big O:**
- O(n) time
  - where n is the number of results
  - we must loop over each item in the results array. operations inside the loop are time-constant regardless of array size.
- O(k) space
  - where k is the number of teams participating
  - we could insert up to k keys in ```points``` as there could be up to k total winners of a match. This results in linear space complexity.