"""

"""
def internship_assignments(interns, teams):
  pairings = []
  remaining = {
    'interns': set({ i for i in range(len(interns))}),
    'teams': set({ t for t in range(len(teams))})  
   }

  pref_start = 0

  while len(remaining['interns']) > 0:
    prefs = {}
    for i in remaining['interns']:
      curr = pref_start

      while curr < len(interns) - 1:
        if interns[i][curr] in remaining['teams']: break
        curr += 1

      top_remaining = interns[i][curr]

      if not top_remaining in prefs: prefs[top_remaining] = set({i})
      else: prefs[top_remaining].update({i})

    for key in prefs:
      idx = 0
      while idx < len(interns):
        if teams[key][idx] in prefs[key] and teams[key][idx] in remaining['interns']:
          team, intern = key, teams[key][idx]
          break
        idx += 1

      remaining['interns'].remove(intern)
      remaining['teams'].remove(team)
      pairings.append([intern, team])
        
    pref_start += 1

  return pairings


if __name__ == "__main__":
  print(internship_assignments(
    [
      [0, 1, 2],
      [1, 0, 2],
      [1, 2, 0]
    ], # interns
    [
      [2, 1, 0],
      [1, 2, 0],
      [0, 2, 1]
    ] # teams
  ))

  print(internship_assignments(
    [
      [0, 1, 2, 3],
      [0, 1, 3, 2], # X
      [0, 2, 3, 1],
      [0, 2, 3, 1]
    ], # interns
    [
      [1, 3, 2, 0], # X
      [0, 1, 2, 3],
      [1, 3, 2, 0],
      [3, 0, 2, 1]
    ] # teams
  )) # [ [1, 0] ]