import random
def diceroll():
  return (random.randint(1,6))

player1 = diceroll()

print (f"Player 1 rolls a {diceroll()}")

import random
def diceroll2():
  return (random.randint(1,6))

player2 = diceroll2()

print (f"Player 2 rolls a {diceroll2()}")

if player1 == player2:
  print("It's a draw!")
elif player1 > player2:
  print (f"Player 1 wins!) ({player1} over {player2}")
else:
  print (f"Player 2 wins! ({player2} over {player1})")
         