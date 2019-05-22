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

L'idée de cette IA était de s'inspirer de plusieurs éléments du document https://github.com/Zamiell/hanabi-conventions permettant de donner un ordre de priorité aux actions à effectuer ainsi qu'un ordre de priorité sur les indices à donner.