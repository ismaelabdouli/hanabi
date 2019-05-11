import hanabi.ai
import hanabi

import itertools

# class AI:
#     """
#     AI base class: some basic functions, game analysis.
#     """
#     def __init__(self, game):
#         self.game = game

#     @property
#     def other_hands(self):
#         "The list of other players' hands."
#         return self.game.hands[1:]

#     @property
#     def other_players_cards(self):
#         "All of other players's cards, concatenated in a single list."
#         #return sum([x.cards for x in self.other_hands], [])
#         return list(itertools.chain.from_iterable([hand.cards for hand in self.other_hands]))


class Player_better:

    def __init__(self, game):
        self.game = game

    @property
    def other_hands(self):
        "The list of other players' hands."
        return self.game.hands[1:]

    @property
    def other_players_cards(self):
        "All of other players's cards, concatenated in a single list."
        #return sum([x.cards for x in self.other_hands], [])
        return list(itertools.chain.from_iterable([hand.cards for hand in self.other_hands]))

    def play(self):
        game = self.game

        number_players = len(game.players)
        number_cards = game.deck.cards_by_player[number_players]
        #il faudra attribuer à chaque main parcourue un nombre entre 0 et (2 * number_cards - 1 )
        #Une main de 4 cartes entraîne par exemple l'attribution d'un numéro entre 0 et 2*4-1=7

        visible = card for card in self.other_players_cards

        #On commence par regarder la main des autres joueurs une par une et à attribuer un nombre correspondant
        for i in range(number_cards):

            #On est dans cette boucle en train de voir la (i+1)eme main après le joueur en train de jouer