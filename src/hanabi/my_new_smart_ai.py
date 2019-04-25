"""
Artificial Intelligence to play Hanabi.
"""

import random

class AI:
    """
    AI base class: some basic functions, game analysis.
    """
    def __init__(self, game):
        self.game = game
        

class Player_random(AI):

    def play(self):
        game = self.game
        
        #On choisit aléatoirement une action à effectuer 
        action=random.choice(["play","discard","give_clue"])
        
        #print(game.blue_coins)
        if action == "play":
            print("I play ! ")
            return("p%d"%random.choice([1,2,3,4,5]))
        
        elif action == "discard":
            print("I discard ! ")
            return("d%d"%random.choice([1,2,3,4,5]))
        
        elif (action == "give_clue") and (game.blue_coins > 0):
            print("I give a clue! ")
           # a="c%s"%random.choice(["W","G","R","Y","B"])
           # print(a)
            #b="c%d"%random.choice([1,2,3,4,5])
            #print(b)
            
            return(random.choice(["c%s"%random.choice(["W","G","R","Y","B"]),"c%d"%random.choice([1,2,3,4,5])]))

        else:
            action=random.choice(["play","discard"])
            if action == "play":
                print("I play ! ")
                return("p%d"%random.choice([1,2,3,4,5]))

            elif action == "discard":
                print("I discard ! ")
                return("d%d"%random.choice([1,2,3,4,5]))

