import hanabi
import hanabi.ai

import statistics

game=hanabi.Game(2)

ai=hanabi.ai.Cheater(game)
L=[]

for i in range(1000):
    #?
    game.ai = ai
    game.run()
    L=L.append(game.score())

print(statistics.mean(L))
