"""
NOTE: this path to a solution did not work
"""
def recursive_determine_p_bust(target, starting_hand, multiplier):
  stand, bust = target - 4, target + 1

  if stand <= starting_hand < bust: return 0

  p_keep_drawing = max(
    round(((stand - 1) - starting_hand) / 10, 3),
    0
  )
  p_bust = max(
    round((1 - .5 - p_keep_drawing) * multiplier, 3),
    0
  )

  if p_keep_drawing > 0:

    for num in range(starting_hand + 1, stand):
      p_bust += recursive_determine_p_bust(
        target,
        num,
        multiplier / 10
      )
  
  print('total p bust', p_bust, starting_hand)

  return round(p_bust, 3)


def blackjack_probability(target, starting_hand):
  first_start = target + 1 - 10
  if starting_hand < first_start: starting_hand = first_start

  return recursive_determine_p_bust(target, starting_hand, 1)


if __name__ == "__main__":
  # print(blackjack_probability(21, 15))

  print(blackjack_probability(21, 14))