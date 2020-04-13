# bridge

def AddNumbers(cards):
  value = {'A': 4, 'K': 3, 'Q': 2, 'J': 1}
  points = 0
  for card in cards:
    if card in ['A', 'K', 'Q', 'J']:
      points += value[card]
  return points

def FindBid(cards):
  suits = cards.split(', ')
  number_of_cards = {0 : 5, 1 : 5, 2 : 3, 3 : 3}
  specific_suit = {0 :'S', 1 :'H', 2 :'D', 3 :'C'}
  for suit, cards in enumerate(suits):
    if len(cards) >= number_of_cards[suit]:
      return '1' + specific_suit[suit]
  return "PASS"

for i in range(5):
  cards = input("Enter cards: ")
  points = AddNumbers(cards)
  bid = FindBid(cards)
  print(points, ', ', bid if points >= 13 else "PASS",sep='')