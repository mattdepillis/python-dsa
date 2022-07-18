"""
Write an algorithm that determines the winner of a tournament in which each team plays every other team exactly once. There will always be one definite winner. A win in a game adds 3 points to the team's total.
Two lists should be passed to the function:
- ```matchups```, which contains nested lists of length 2: [home_team, away_team]
- ```results```, which is a list of the results from the games. results[0] corresponds to the result of the first game. 1 means the home_team won; 0 means the away_team won.

Return the name of the winning team.
"""
def tournament_winner(matchups, results):
  points = {}
  for i in range(len(results)):
    winner = matchups[i][0] if results[i] == 1 else matchups[i][1]
    if winner not in points:
      points[winner] = 3
    else:
      points[winner] += 3

  return max(points, key=points.get)

if __name__ == "__main__":
  # print(tournament_winner([
  #   ['Eagles', 'Cowboys'],
  #   ['Dolphins', 'Eagles'],
  #   ['Cowboys', 'Dolphins']
  # ], [1, 0, 0]))
  print(tournament_winner([
  ["AlgoMasters", "FrontPage Freebirds"],
  ["Runtime Terror", "Static Startup"],
  ["WeC#", "Hypertext Assassins"],
  ["AlgoMasters", "WeC#"],
  ["Static Startup", "Hypertext Assassins"],
  ["Runtime Terror", "FrontPage Freebirds"],
  ["AlgoMasters", "Runtime Terror"],
  ["Hypertext Assassins", "FrontPage Freebirds"],
  ["Static Startup", "WeC#"],
  ["AlgoMasters", "Static Startup"],
  ["FrontPage Freebirds", "WeC#"],
  ["Hypertext Assassins", "Runtime Terror"],
  ["AlgoMasters", "Hypertext Assassins"],
  ["WeC#", "Runtime Terror"],
  ["FrontPage Freebirds", "Static Startup"]
], [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]))