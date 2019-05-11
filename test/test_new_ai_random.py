
# bien faire un "make module"

import hanabi
import hanabi.ai

import hanabi.random_ai as new_ai

game = hanabi.Game(2)  # 2 players

ai = new_ai.Player_random(game)
#ai = hanabi.ai.Cheater(game)


#ai.play()

# pour jouer juste un tour:
#game.turn()      # prompt
#game.turn(ai)    # c'est l'ai qui joue
#game.turn('c1')  # ou je peux donner une commande
#game.turn(['c1', 'c2', 'p2'])  # ... ou toute une serie 

# pour jouer toute une partie
game.ai = ai

#faire alors sur python3 : from test_new_ai_random import *
