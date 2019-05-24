import hanabi
import hanabi.ai

import statistics

import matplotlib.pyplot as plt
import numpy as np

L=[]
game=hanabi.Game(2)
import hanabi.ai_mieux as new_ai

for i in range(1000):
    game.reset()
    game=hanabi.Game(2)
    game.quiet=True
    ai=new_ai.Player_better(game)
    game.ai = ai
    game.run()
    L.append(game.score)

print(statistics.mean(L))
#X=[]
# for i in range(max(L)+1):
#     X.append[L.count(i)]
# plt.plot(X,range(max(L)+1))
plt.hist(L)
plt.title('Statistiques pour Player better')
plt.savefig('stat_better_2.png')
plt.show()