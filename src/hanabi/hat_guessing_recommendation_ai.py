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

        #il faudra attribuer à chaque main parcourue un nombre entre 0 et (2 * number_cards - 1 )
        #Une main de 4 cartes entraîne par exemple l'attribution d'un numéro entre 0 et 2*4-1=7

        visible = [card for card in self.other_players_cards]
        number_players = len(game.players)
        number_cards = game.deck.cards_by_player[number_players]

    def give_a_clue(self,game,visible,number_players,number_cards):    

        #On commence par regarder la main des autres joueurs une par une et à attribuer un nombre correspondant
        for i in range(number_players):
            
            #S est la somme des couleurs (ou chapeau) des autres joueurs
            S=0
            rank_lowest = 1000
            rank_lowest_2 = 1000
            hint_to_players = [0] * (number_players-1)
            important_card = None
            type_recommendation = 10 #10 sera change si on n'arrive pas a la recommendation 5 (ce n'est qu'une attribution temporaire)

            for k in range(i*number_cards,(i+1)*number_cards):
            #On est dans cette boucle en train de voir la (i+1)eme main après le joueur en train de jouer

                card=visible[k]

                #we search the playable card of rank 5 with lowest index play.
                if game.piles[card.color]+1 == card.number and card.number == 5:
                    hat_color = k%number_cards
                    important_card = card
                    type_recommendation = 1

                #if recommendation of type 1 is impossible, then we search the playable card with lowest rank and with lowest index
                elif game.piles[card.color]+1 == card.number and card.number<rank_lowest and type_recommendation >= 2:
                    hat_color = k%number_cards
                    rank_lowest = card.number
                    important_card = card
                    type_recommendation = 2

                #if recommendation of type 2 is impossible, then we search the dead card with lowest index
                elif game.piles[card.color] >= card.number and type_recommendation >= 3:
                    hat_color = k%number_cards + number_cards
                    important_card = card
                    type_recommendation = 3

                #on compte le nombre de cartes identiques à celle que l'on considère dans la pile de défausse
                for card_from_discard in game.discard_pile.cards:
                    if card_from_discard == card:
                        count += 1

                #if recommendation of type 3 is impossible, then we search the highest rank and the lowest index that is not indispensable
                if (count == game.deck.card_count[card.number]-1) and card.number > rank_lowest_2 and type_recommendation >= 4: #si oui, alors c'est la derni�re carte, qui n'a obligatoirement pas �t� jou�e car toutes les autres sont dans la pile
                    important_card = card
                    hat_color = k%number_cards + number_cards
                    rank_lowest_2 = card.number
                    type_recommendation = 4

            #if recommendation of type 4 is impossible, then we recommend to dicard c1 by default
            if important_card == None :
                important_card = visible[i*number_cards]
                hat_color = number_cards + number_cards #c1 discard
                #type_recommendation = 5
            
            hint_to_players[i] = hat_color % number_cards #commence a 0

            S += hat_color

        S = S % number_cards

        type_recommendation_4cards = {0 : (important_card.number,0),
                                      1 : (important_card.number,1),
                                      2 : (important_card.number,2),
                                      3 : (important_card.number,3),
                                      4 : (important_card.color,0),
                                      5 : (important_card.color,1),
                                      6 : (important_card.color,2),
                                      7 : (important_card.color,3)}

        type_recommendation_5cards = {0 : (important_card.number,0),
                                      1 : (important_card.number,1),
                                      2 : (important_card.number,2),
                                      3 : (important_card.number,3),
                                      4 : (important_card.number,4),
                                      5 : (important_card.color,0),
                                      6 : (important_card.color,1),
                                      7 : (important_card.color,2),
                                      8 : (important_card.color,3),
                                      9 : (important_card.color,4)}







                


 