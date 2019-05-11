import hanabi
import hanabi.ai

import statistics

L=[]
game=hanabi.Game(5)
import hanabi.ai_vraiment_mieux as new_ai

for i in range(1000):
    game.reset()
    game=hanabi.Game(5)
    game.quiet=True
    ai=new_ai.Player_better(game)
    game.ai = ai
    game.run()
    L.append(game.score)

print(statistics.mean(L))