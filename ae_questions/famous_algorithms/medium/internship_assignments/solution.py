"""

"""
def internship_assignments(interns, teams):
  pairings = []
  remaining = {
    'interns': set({ i for i in range(len(interns))}),
    'teams': set({ t for t in range(len(teams))})
   }

  while len(remaining['interns']) > 0:
    prefs = {}
    for i in remaining['interns']:
      curr = 0

      while curr < len(interns) - 1:
        if interns[i][curr] in remaining['teams']: break
        curr += 1

      top_remaining = interns[i][curr]
      if not top_remaining in prefs:
        prefs[top_remaining] = set({i})
      else: prefs[top_remaining].update({i})

    for key in prefs:
      idx = 0
      while idx < len(interns):
        preferred_intern = teams[key][idx]
        if preferred_intern in prefs[key] and preferred_intern in remaining['interns']:
          team, intern = key, preferred_intern
          break
        idx += 1

      remaining['interns'].remove(intern)
      remaining['teams'].remove(team)
      pairings.append([intern, team])

      if len(prefs[key]) > 1: break

  return pairings


if __name__ == "__main__":
  print(internship_assignments(
    [
      [0, 1, 2, 3],
      [2, 1, 3, 0],
      [0, 2, 3, 1],
      [3, 1, 0, 2]
    ],
    [
      [1, 3, 2, 0],
      [0, 1, 2, 3],
      [1, 2, 3, 0],
      [3, 0, 2, 1]
    ]
  ))

  # print(internship_assignments(
  #   [
  #     [0, 1, 2],
  #     [0, 2, 1],
  #     [1, 2, 0]
  #   ],
  #   [
  #     [2, 1, 0],
  #     [0, 1, 2],
  #     [0, 2, 1]
  #   ]
  # ))


  # print(internship_assignments(
  #   [
  #     [0, 1, 2],
  #     [1, 0, 2],
  #     [1, 2, 0]
  #   ], # interns
  #   [
  #     [2, 1, 0],
  #     [1, 2, 0],
  #     [0, 2, 1]
  #   ] # teams
  # ))

  # print(internship_assignments(
  #   [
  #     [0, 1, 2, 3],
  #     [0, 1, 3, 2], # X
  #     [0, 2, 3, 1],
  #     [0, 2, 3, 1]
  #   ], # interns
  #   [
  #     [1, 3, 2, 0], # X
  #     [0, 1, 2, 3],
  #     [1, 3, 2, 0],
  #     [3, 0, 2, 1]
  #   ] # teams
  # )) # [ [1, 0] ]