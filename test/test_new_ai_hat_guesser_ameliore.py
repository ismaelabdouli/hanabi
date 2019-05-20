
# bien faire un "make module"

import hanabi
import hanabi.ai

import hanabi.ai_hat_guessing_recommendation_ameliore as new_ai

game = hanabi.Game(5)  # 2 players

ai = new_ai.Player_hat_guesser(game)
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
