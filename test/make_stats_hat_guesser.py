import hanabi
import hanabi.ai

import statistics
import matplotlib.pyplot as plt

L=[]
game=hanabi.Game(5)
import hanabi.ai_hat_guessing_recommendation as new_ai

for i in range(1000):
    game.reset()
    game=hanabi.Game(5)
    game.quiet=True
    ai=new_ai.Player_hat_guesser(game)
    game.ai = ai
    game.run()
    L.append(game.score)

print(statistics.mean(L))
plt.hist(L)
plt.title('Statistiques pour Player hat guesser')
plt.savefig('stat_hat_guesser_1.png')
plt.show()