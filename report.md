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

Voici pour 1000 parties la courbe de répartition des scores :

![Figure 1 - 5 joueurs](https://github.com/ismaelabdouli/hanabi/blob/master/test/stat_better_1.png)
Avec un score moyen de 5,12 sur 1000 parties, score allant de 2 à 10

![Figure 2 - 2 joueurs](https://github.com/ismaelabdouli/hanabi/blob/master/test/stat_better_2.png)
Avec un score moyen de 8,86 sur 1000 parties, score allant de 4 à 14
