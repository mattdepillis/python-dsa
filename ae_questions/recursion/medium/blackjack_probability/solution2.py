"""
Find the probability of busting in the game of blackjack when given a starting hand and a target top number to hit.

TC: O(t - s), where t = target and s = starting_hand.
  - because we recurse t - s levels-proportionally deep
SC: O(t - s): hold t - s calls on the stack at maximum
"""
def determine_bust(target, starting_hand, records):
  if starting_hand in records: return records[starting_hand]
  elif starting_hand > target: return 1
  elif starting_hand + 4 >= target: return 0

  p_bust = 0
  for num in range(1, 11):
    p_bust += determine_bust(target, starting_hand + num, records) * .1

  records[starting_hand] = p_bust
  
  return p_bust

def blackjack_probability(target, starting_hand):
  records = {}
  p = round(determine_bust(target, starting_hand, records), 3)
  print(records)
  return p


if __name__ == "__main__":
  print(blackjack_probability(21, 12))