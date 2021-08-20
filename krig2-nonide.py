#python 3.7.1

import random
from tqdm import tqdm

class Card:
  def __init__(self, type, value) -> None:
    self.type = type
    self.value = value
   
  def __repr__(self) -> str:
    return f"{self.type} {self.value}"


class Player:
  
  def __init__(self) -> None:
    self.deck = []
    self.wins = []
  
  def flip(self) -> Card:
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


class Game:
  
  def __init__(self):
    self.player1 = Player()
    self.player2 = Player()
    
    self.total = 1
    
    self.deck = []
    #populate deck
    for i in ["c", "h", "d", "s"]:
      for j in range(13):
        self.deck.append(Card(i, j + 1))
    
  def setup(self):
    #shuffle deck
    random.shuffle(self.deck)
    
    #reset number of times played
    self.total = 1
    
    #distribute cards between players
    self.player1.deck = self.deck[:26]
    self.player2.deck = self.deck[26:]

  def play(self):
    #play rounds
    while not self.player1.isEmpty() and not self.player2.isEmpty():

      a = self.player1.flip()
      b = self.player2.flip()
  
      at_stake_p1 = [a]
      at_stake_p2 = [b]
  
      while a.value == b.value:
        at_stake_p1.extend([self.player1.flip() for i in range(min(3, self.player1.getTotal()))])
        a = at_stake_p1[-1]
    
        at_stake_p2.extend([self.player2.flip() for i in range(min(3, self.player2.getTotal()))])
        b = at_stake_p2[-1]
    
      if a.value > b.value:
        self.player1.wins.extend(at_stake_p1 + at_stake_p2)
      else:
        self.player2.wins.extend(at_stake_p1 + at_stake_p2)
    
      self.total += 1
    return self.total
 
game = Game()
dist = {}

for i in tqdm(range(2500)):
  game.setup()
  num = game.play()
  dist[num] = 1 if not dist.get(num) else dist[num]+1

for i in sorted(dist):
  print(f"{i}: " + dist[i] * "*")