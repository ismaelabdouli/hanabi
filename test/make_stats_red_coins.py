import hanabi
import hanabi.ai

import statistics

import matplotlib.pyplot as plt

L=[]
game=hanabi.Game(5)
import hanabi.ai_hat_guessing_recommendation_ameliore as new_ai

for i in range(1000):
    game.reset()
    game=hanabi.Game(5)
    game.quiet=True
    ai=new_ai.Player_hat_guesser(game)
    game.ai = ai
    game.run()
    L.append(game.red_coins)

print(statistics.mean(L))
plt.hist(L)
plt.title('Statistiques pour le nombre de jetons rouges finaux du hat guesser')
plt.savefig('red_coins_hat_guesser.png')
plt.show()