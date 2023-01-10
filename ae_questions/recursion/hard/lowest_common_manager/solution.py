"""

"""
class Node:
  def __init__(self, name):
    self.name = name
    self.reports = []

def search_for_node(reports, node_to_find):
  for r in reports:
    if node_to_find in reports:
      return True
    if search_for_node(r.reports, node_to_find): return True
  return False

def recurse(node, r1, r2):
  if node == r1 or node == r2:
    to_find = r1 if node == r2 else r1
    is_parent = search_for_node(node.reports, to_find)
    return node, is_parent
  else:
    found = []
    for report in node.reports:
      (n, found_both) = recurse(report, r1, r2)
      if found_both: return n, True
      elif n: found.append(node)
    if len(found) == 2: return node, True
    elif len(found) == 1: return found[0], False
  return None, False

def lowest_common_manager(node, r1, r2):
  # (n, found) = recurse(node, r1, r2)
  # return n.name if found else node.name
  return recurse(node, r1, r2)[0]
  


if __name__ == "__main__":
  nodes = [
    {"directReports": ["B", "C"], "id": "A", "name": "A"},
    {"directReports": ["D", "E"], "id": "B", "name": "B"},
    {"directReports": ["F", "G"], "id": "C", "name": "C"},
    {"directReports": ["H", "I"], "id": "D", "name": "D"},
    {"directReports": [], "id": "E", "name": "E"},
    {"directReports": [], "id": "F", "name": "F"},
    {"directReports": [], "id": "G", "name": "G"},
    {"directReports": [], "id": "H", "name": "H"},
    {"directReports": [], "id": "I", "name": "I"}
  ]
  # nodes = [
  #   {"directReports": ["B", "C", "D", "E", "F"], "id": "A", "name": "A"},
  #   {"directReports": ["G", "H", "I"], "id": "B", "name": "B"},
  #   {"directReports": ["J"], "id": "C", "name": "C"},
  #   {"directReports": ["K", "L"], "id": "D", "name": "D"},
  #   {"directReports": [], "id": "E", "name": "E"},
  #   {"directReports": ["M", "N"], "id": "F", "name": "F"},
  #   {"directReports": [], "id": "G", "name": "G"},
  #   {"directReports": ["O", "P", "Q", "R"], "id": "H", "name": "H"},
  #   {"directReports": [], "id": "I", "name": "I"},
  #   {"directReports": [], "id": "J", "name": "J"},
  #   {"directReports": ["S"], "id": "K", "name": "K"},
  #   {"directReports": [], "id": "L", "name": "L"},
  #   {"directReports": [], "id": "M", "name": "M"},
  #   {"directReports": [], "id": "N", "name": "N"},
  #   {"directReports": [], "id": "O", "name": "O"},
  #   {"directReports": ["T", "U"], "id": "P", "name": "P"},
  #   {"directReports": [], "id": "Q", "name": "Q"},
  #   {"directReports": ["V"], "id": "R", "name": "R"},
  #   {"directReports": [], "id": "S", "name": "S"},
  #   {"directReports": [], "id": "T", "name": "T"},
  #   {"directReports": [], "id": "U", "name": "U"},
  #   {"directReports": ["W", "X", "Y"], "id": "V", "name": "V"},
  #   {"directReports": [], "id": "W", "name": "W"},
  #   {"directReports": ["Z"], "id": "X", "name": "X"},
  #   {"directReports": [], "id": "Y", "name": "Y"},
  #   {"directReports": [], "id": "Z", "name": "Z"}
  # ]

  store, report_store = {}, {}

  for node in nodes:
    name = node["name"]
    store[name] = Node(name)
    report_store[name] = node["directReports"]

  for node in store:
    for report in report_store[node]:
      store[node].reports = store[node].reports + [store[report]]

  # for node in store:
  #   for report in store[node].reports:
  #     print(node, report.name)

  print(lowest_common_manager(store['A'], store['E'], store['I']))
  # print(lowest_common_manager(store['A'], store['Z'], store['B']))