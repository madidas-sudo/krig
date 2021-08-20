import random

total = 1

class Player:
  
  def __init__(self) -> None:
    self.deck = []
    self.wins = []
  
  def flip(self):
    #returns card object
    if (not self.deck) and self.wins:
      #redistribute wins to deck and shuffle
      self.deck = random.sample(self.wins, len(self.wins))
      self.wins = []
    return self.deck.pop()
    
  def isEmpty(self) -> bool:
    return True if self.getTotal() == 0 else False
    
  def getTotal(self) -> int:
    return len(self.deck) + len(self.wins)

class Card:
  def __init__(self, type, value) -> None:
    self.type = type
    self.value = value
   
  def __repr__(self) -> str:
    return f"{self.type} {self.value}"

player1 = Player()
player2 = Player()
   
deck = []

#populate deck
for i in ["c", "h", "d", "s"]:
  for j in range(13):
    deck.append(Card(i, j + 1))
    
#shuffle deck
random.shuffle(deck)

#distribute cards between players
player1.deck = [i for i in deck[:int(len(deck)/2)]]
player2.deck = [i for i in deck[int(len(deck)/2):]]

#play rounds
while not player1.isEmpty() and not player2.isEmpty():

  #catch error for debugging
  if not player1.getTotal() + player2.getTotal() == 52:
    raise Exception("total cards is not equal to 52")

  print(f"player 1 total: {player1.getTotal()} player 2 total: {player2.getTotal()}")
  
  a = player1.flip()
  b = player2.flip()
  
  at_stake_a = [a]
  at_stake_b = [b]
  
  while a.value == b.value:
    print("krig!")

    at_stake_a.extend([player1.flip() for i in range(min(3, player1.getTotal()))])
    a = at_stake_a[-1]
    
    at_stake_b.extend([player2.flip() for i in range(min(3, player2.getTotal()))])
    b = at_stake_b[-1]
    
  if a.value > b.value:
    player1.wins.extend(at_stake_a + at_stake_b)
  else:
    player2.wins.extend(at_stake_a + at_stake_b)
    
  total += 1
 
print(f"total times played: {total}")