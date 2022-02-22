"""
  1. Write a function that creates a deck of cards from a tuple of suits and tuple of values,
  and return said deck of cards in randomized order.
"""
import random
suits = ("Hearts", "Spades", "Clubs", "Diamonds")
values = (2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace")

def shuffle_deck(suits, values):
  deck = []
  shuffled_deck = []

  for suit in suits:
    for value in values:
      deck.append("{} of {}".format(value, suit))

  while (len(deck) > 0):
    index = random.randrange(0, len(deck))
    shuffled_deck.append(deck[index])
    deck.pop(index)

  return shuffled_deck


###################################################################################################################################
"""
  2. Sieve of Eratosthenes using a list.
"""