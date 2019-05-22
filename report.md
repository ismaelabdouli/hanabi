# Rapport

## AI Random

### Description

Cette IA joue aléatoirement. On choisit d'abord le type de coup à effectuer au hasard (jouer, défausser ou donner un indice).
Ensuite, si on joue ou on défausse, l'IA choisit au hasard la carte de sa main à sélectionner. Sinon, on choisit au hasard (s'il y a assez de jetons bleus) un indice à donner. A noter qu'il est possible de donner par exemple un indice de couleur ou de nombre non présents dans la main.

### Score

Evidemment, nous obtenons un score moyen de 0 sur 1000 parties.

### Discussion

Si le fait de piocher 3 jetons rouges ne ramenait pas le score à 0 mais arrêtait quand même la partie, l'IA random aurait un score maximal de 8 et ferait deux tiers des parties à score non nul.

## AI BOFENFAIT

### Description and Discussion

L'idée de cette IA était de s'inspirer de plusieurs éléments du document https://github.com/Zamiell/hanabi-conventions permettant de donner un ordre de priorité aux actions à effectuer ainsi qu'un ordre de priorité sur les indices à donner. L'IA était censée ne jouait que les cartes dont elle connaissait rang et couleur, donc elle ne devait jamais se tromper. Cependant, nous avions des difficultés à la rendre fonctionnelle lors du parcours des mains des autres joueurs.
En effet, nous ne disposions pas encore de la fonction "other_players_cards" permettant d'obtenir une liste unique des mains visibles, supportant l'indexation. Nous n'avions donc pas un indice de liste unique pour chaque carte considérée. Par exemple, la carte d'index 2 de Alice et de Benji avait le même indice de liste mais était dans deux listes différentes. Cela complexifiait notre réflexion et nous avons décider de refaire cette IA avec une liste unique de la main des joueurs.

## AI VRAIMENTMIEU

### Description

Le principe de cette IA est donc le même que la précédente IA : donner un indice est la priorité. On distingue les "save clues" des "play clues". On suppose qu'il faut éviter de défausser les cartes indicées. Les "save clues", à faire avant les "play clues", visent donc à éviter de défausser certaines cartes, ce sont par ordre de priorité : 
1. Les 5
2. Les 2 (uniquement si on ne voit pas cette carte ailleurs)
3. Les cartes qui sont le dernier exemplaire encore jouable dans la partie (tous les autres exemplaires ont été défaussés)
4. Les cartes pas encore jouées qui ne sont visibles nulle part ailleurs dans la main des joueurs.

Les "play clues" correspondent aux cartes jouables immédiatemment.
Pour donner les indices, on donne en priorité un indice sur le rang de la carte. Sinon, on donne un indice sur sa couleur. On cherche d'abord à indicer la "chop card" (la plus vieille carte sans indice), sinon on cherche à indicer les cartes les plus récentes des mains.

Si rien de tout cela n'est possible, ou s'il ne reste aucun jeton bleu, on joue les cartes connues et jouables de sa main.

Si on ne peut jouer aucune carte, on défausse la "chop card".

### Simulation

Voici, pour 1000 parties, la courbe de répartition des scores :

![Figure 1 - 5 joueurs](https://github.com/ismaelabdouli/hanabi/blob/master/test/stat_better_1.png)

Avec un score moyen de 5,12 sur 1000 parties, score allant de 2 à 10.

![Figure 2 - 2 joueurs](https://github.com/ismaelabdouli/hanabi/blob/master/test/stat_better_2.png)

Avec un score moyen de 8,86 sur 1000 parties, score allant de 4 à 14.

### Discussion

Cette méthode a l'avantage d'éviter de perdre une partie sans utiliser un programme complexe. Cependant, elle paraît loin d'être optimale car elle prend en compte un nombre assez limité d'idées pour donner les indices. Ainsi, il est impossible ici d'éviter de jeter des cartes intéressantes.

## AI Hat Guessing Recommendation

### Desciption

Cette IA se base sur le jeu du hat guessing, présenté sur le pdf : https://sites.google.com/site/rmgpgrwc/research-papers/Hanabi_final.pdf?attredirects=1. On attribue à chaque joueur une "couleur" (un numéro) correspondant au coup que l'on veut qu'il effectue. On fait la somme de ces numéros sur tous les joueurs visibles et cela nous donne un code correspondant à l'indice que l'on doit donner. Chaque joueur sait interpréter cet indice comme consigne individuelle car il voit les "couleurs" des autres joueurs et en déduit la sienne.

On utilise cet ordre de priorité sur les actions à effectuer :
1. Si la recommendation la plus récente était de jouer une carte et qu'aucune carte n'a été jouée depuis le dernier indice, jouer la carte recommandée.
2. Si la recommendation la plus récente était de jouer une carte et qu'une carte a été jouée depuis le dernier indice, et que les joueurs ont moins de 2 jetons rouges, jouer la carte recommandée.
3. Si les joueurs ont un jeton bleu, donner un indice.
4.  Si la recommendation la plus récente était de défausser une carte, défausser la carte recommandée.
5. Défausser la plus vieille carte de sa main (donc d'index 1).

### Simulation

Voici, pour 1000 parties, la courbe de répartition des scores :

![Figure 3 - 5 joueurs](https://github.com/ismaelabdouli/hanabi/blob/master/test/stat_hat_guesser_ameliore_3.png)

Avec un score moyen de 22,25 sur 1000 parties, score allant de 15 à 25.

### Discussion

On arrive à un score très satisfaisant, mais légèrement moindre que celui donné dans l'article susmentionné. Cela est peut-être dû au dernier tour, pour lequel on applique strictement la même méthode qu'au tour précédent, ce qui n'est pas forcément optimal. De plus, lors de ce dernier tour, nous avons décidé, pour avoir une liste des cartes des autres joueurs de même taille, même lorsqu'un joueur a une carte de moins, de lui rajouter une carte virtuelle (Yellow,0). Si on tombe sur cette carte ensuite, on ne la considère pas.

Il faut noter que cette IA ne peut jouer qu'à 5 joueurs car on doit avoir un code qui décrit toutes les actions qu'un joueur peut effectuer. Ainsi, un joueur peut jouer ou défausser chaque carte de sa main, ce qui nécessite un code à 8 nombres pour 4 et 5 joueurs, et un code à 10 nombres pour 2 et 3 joueurs. Le code s'exprimant sur le type d'indice (deux possibilités : rang ou couleur) que l'on donne, et le numéro du joueur à qui on le donne, on manque de possibilités s'il y a moins de 5 joueurs. Pour remédier à cela, on pourrait utiliser la hat guessing strategy où l'on donne un indice au joueur suivant peu importe les cas. Le code serait alors déduit du type "complet" d'indice (10 possibilités : chaque couleur, chaque rang). Nous avons cependant manqué de temps pour l'implémenter. 