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
from hanabi.ai import AI 

class Player_hat_guesser(AI):

    def __init__(self, game):
        self.game = game
        self.latest_turn_memory=[0,0,-1] #A chaque tour, ce couple represente (nombre de cartes posees depuis le dernier indice, nombre de cartes defaussees depuis le dernier indice, le dernier indice sous forme de "couleur" (initiliasee de facon fantaisiste))
        #On fait la somme des deux premiers elements du couple pour obtenir le nombre de coups effectues depuis le dernier indice.
        self.list_players = ['Alice','Benji','Clara','Dante','Elric']
        self.list_players = self.list_players[0:len(game.players)]
        self.what_to_do = [1000]*(len(game.players)-1)


    @property
    def other_hands(self):
        "The list of other players' hands."
        return self.game.hands[1:]

    def recommendation_4cards(self,i):
        type_recommendation_4cards = {0 : ('number',0),
                                      1 : ('number',1),
                                      2 : ('number',2),
                                      3 : ('number',3),
                                      4 : ('color',0),
                                      5 : ('color',1),
                                      6 : ('color',2),
                                      7 : ('color',3)}
        return type_recommendation_4cards[i]

    def recommendation_5cards(self,i):
        type_recommendation_5cards = {0 : ('number',0),
                                      1 : ('number',1),
                                      2 : ('number',2),
                                      3 : ('number',3),
                                      4 : ('number',4),
                                      5 : ('color',0),
                                      6 : ('color',1),
                                      7 : ('color',2),
                                      8 : ('color',3),
                                      9 : ('color',4)}
        return type_recommendation_5cards[i]

    @property
    def other_players_cards(self):
        "All of other players's cards, concatenated in a single list."
        #return sum([x.cards for x in self.other_hands], [])
        return list(itertools.chain.from_iterable([hand.cards for hand in self.other_hands]))




    def play(self):
        game = self.game

        self.list_players.append(self.list_players[0])
        self.list_players.pop(0)#On modifie la liste des noms pour qu'elle commence par le premier joueur qu'on observe et finisse par nous
        #il faudra attribuer à chaque main parcourue un nombre entre 0 et (2 * number_cards - 1 )
        #Une main de 4 cartes entraîne par exemple l'attribution d'un numéro entre 0 et 2*4-1=7

        visible = [card for card in self.other_players_cards]
        number_players = len(game.players)
        number_cards = game.deck.cards_by_player[number_players]
        virtual_card = hanabi.deck.Card(hanabi.deck.Color.Yellow,0)  


        if len(game.deck.cards) != 0:
        
            ###DEBUT GIVE A CLUE ###
            #On commence par regarder la main des autres joueurs une par une et à attribuer un nombre correspondant

            #S est la somme des couleurs (ou chapeau) des autres joueurs
            S=0
            color_by_players = [0] * (number_players-1)
            for i in range(number_players-1):
                
                rank_lowest = 1000
                rank_lowest_2 = 1000
                type_recommendation = 10 #10 sera change si on n'arrive pas a la recommendation 5 (ce n'est qu'une attribution temporaire)

                for k in range(i*number_cards,(i+1)*number_cards):
                #On est dans cette boucle en train de voir la (i+1)eme main après le joueur en train de jouer

                    card=visible[k]

                    #we search the playable card of rank 5 with lowest index play.
                    if game.piles[card.color]+1 == card.number and card.number == 5:
                        hat_color = k%number_cards
                        type_recommendation = 1

                    #if recommendation of type 1 is impossible, then we search the playable card with lowest rank and with lowest index
                    elif game.piles[card.color]+1 == card.number and card.number<rank_lowest and type_recommendation >= 2:
                        hat_color = k%number_cards
                        rank_lowest = card.number
                        type_recommendation = 2

                    #if recommendation of type 2 is impossible, then we search the dead card with lowest index
                    elif game.piles[card.color] >= card.number and type_recommendation > 3:
                        hat_color = k%number_cards + number_cards
                        type_recommendation = 3

                    #on compte le nombre de cartes identiques à celle que l'on considère dans la pile de défausse
                    count=0
                    for card_from_discard in game.discard_pile.cards:
                        if card_from_discard == card:
                            count += 1

                    #if recommendation of type 3 is impossible, then we search the highest rank and the lowest index that is not indispensable
                    if (count == game.deck.card_count[card.number]-1) and card.number > rank_lowest_2 and type_recommendation >= 4: #si oui, alors c'est la derni�re carte, qui n'a obligatoirement pas �t� jou�e car toutes les autres sont dans la pile
                        hat_color = k%number_cards + number_cards
                        rank_lowest_2 = card.number
                        type_recommendation = 4

                #if recommendation of type 4 is impossible, then we recommend to discard c1 by default
                if type_recommendation == 10 :
                    hat_color = number_cards #c1 discard
                    #type_recommendation = 5
                
                color_by_players[i] = hat_color #commence a 0

                S += hat_color

            S = S % (2*number_cards)

            ### FIN GIVE A CLUE ###

            ### DEBUT WHAT TO DO ###
            index_what_to_do = self.latest_turn_memory[0]+self.latest_turn_memory[1]
            if self.what_to_do[index_what_to_do] <= number_cards and self.latest_turn_memory[0]==0: #If the most recent recommendation was to play a card and no card has been played since the last hint, play the recommended card
                self.latest_turn_memory[0] += 1
                return('p%d'%self.what_to_do[index_what_to_do])
                #return ('c{}'.format(what_to_do))

            elif self.what_to_do[index_what_to_do] <= number_cards and self.latest_turn_memory[0]==1 and game.red_coins<2 : #If the most recent recommendation was to play a card, one card has been played since the hint was given, and the players have made fewer than two errors, play the recommended card
                self.latest_turn_memory[0]+=1
                return('p%d'%self.what_to_do[index_what_to_do])
                #return ('c{}'.format(what_to_do))
            
            elif game.blue_coins > 0 : #If the players have a hint token, give a hint
                self.latest_turn_memory=[0,0,S]
                if number_cards == 4 :
                    recommendation = self.recommendation_4cards(S)
                else :
                    recommendation = self.recommendation_5cards(S)
                card_to_hint=visible[recommendation[1]*number_cards] #on donne un indice sur la premiere carte du joueur considere
                if recommendation[0]=='number':

                    for j in range(number_players-1):
                        what_to_do_j = self.latest_turn_memory[2]
                        players_not_hinters_j = [i for i in range(number_players-1) if i != j]
                        for i in players_not_hinters_j: #on considère tous les autres joueurs sauf celui qui a donné le dernier indice
                            what_to_do_j -= color_by_players[i]
                        what_to_do_j %= (2*number_cards)
                        what_to_do_j += 1
                        self.what_to_do[j] = what_to_do_j

                    return ('c{}{}'.format(card_to_hint.number,self.list_players[recommendation[1]][0]))
                if recommendation[0]=='color':

                    for j in range(number_players-1):
                        what_to_do_j = self.latest_turn_memory[2]
                        players_not_hinters_j = [i for i in range(number_players-1) if i != j]
                        for i in players_not_hinters_j: #on considère tous les autres joueurs sauf celui qui a donné le dernier indice
                            what_to_do_j -= color_by_players[i]
                        what_to_do_j %= (2*number_cards)
                        what_to_do_j += 1
                        self.what_to_do[j] = what_to_do_j

                    return ('c{}{}'.format(str(card_to_hint.color)[0],self.list_players[recommendation[1]][0]))
                
            elif self.what_to_do[index_what_to_do] > number_cards : #If the most recent recommendation was to discard a card, discard the requested card
                self.latest_turn_memory[1]+=1
                return('d%d'%(self.what_to_do[index_what_to_do]-number_cards))
                #return ('c{}'.format(what_to_do))
            
            else : #Otherwise, discard c1
                self.latest_turn_memory[1]+=1
                return('d1')
            ### FIN WHAT TO DO ###

        
        #On rentre ici si c'est le dernier tour
        else :
            ###DEBUT GIVE A CLUE ###
            #On commence par regarder la main des autres joueurs une par une et à attribuer un nombre correspondant

            #S est la somme des couleurs (ou chapeau) des autres joueurs
            S=0
            color_by_players = [0] * (number_players-1)
            for i in range(number_players-1):
                
                rank_lowest = 1000
                rank_lowest_2 = 1000
                type_recommendation = 10 #10 sera change si on n'arrive pas a la recommendation 5 (ce n'est qu'une attribution temporaire)

                for k in range(i*number_cards,(i+1)*number_cards):
                #On est dans cette boucle en train de voir la (i+1)eme main après le joueur en train de jouer

                    card=visible[k]

                    #we search the playable card of rank 5 with lowest index play.
                    if card != virtual_card and game.piles[card.color]+1 == card.number and card.number == 5:
                        hat_color = k%number_cards
                        type_recommendation = 1

                    #if recommendation of type 1 is impossible, then we search the playable card with lowest rank and with lowest index
                    elif card != virtual_card and game.piles[card.color]+1 == card.number and card.number<rank_lowest and type_recommendation >= 2:
                        hat_color = k%number_cards
                        rank_lowest = card.number
                        type_recommendation = 2

                    #if recommendation of type 2 is impossible, then we search the dead card with lowest index
                    elif card != virtual_card and game.piles[card.color] >= card.number and type_recommendation > 3:
                        hat_color = k%number_cards + number_cards
                        type_recommendation = 3

                    #on compte le nombre de cartes identiques à celle que l'on considère dans la pile de défausse
                    count=0
                    for card_from_discard in game.discard_pile.cards:
                        if card_from_discard == card:
                            count += 1

                    #if recommendation of type 3 is impossible, then we search the highest rank and the lowest index that is not indispensable
                    if  card != virtual_card and (count == game.deck.card_count[card.number]-1) and card.number > rank_lowest_2 and type_recommendation >= 4: #si oui, alors c'est la derni�re carte, qui n'a obligatoirement pas �t� jou�e car toutes les autres sont dans la pile
                        hat_color = k%number_cards + number_cards
                        rank_lowest_2 = card.number
                        type_recommendation = 4

                #if recommendation of type 4 is impossible, then we recommend to discard c1 by default
                if type_recommendation == 10 :
                    hat_color = number_cards #c1 discard
                    #type_recommendation = 5
                
                color_by_players[i] = hat_color #commence a 0

                S += hat_color

            S = S % (2*number_cards)

            ### FIN GIVE A CLUE ###


            ### DEBUT WHAT TO DO ###
            index_what_to_do = self.latest_turn_memory[0]+self.latest_turn_memory[1]
            if self.what_to_do[index_what_to_do] <= number_cards and self.latest_turn_memory[0]==0: #If the most recent recommendation was to play a card and no card has been played since the last hint, play the recommended card
                self.latest_turn_memory[0] += 1
                game.current_hand.cards.append(virtual_card) #on rajoute une carte "virtuelle" pour conserver le même nombre de cartes total (len(visible) = constante)
                return('p%d'%self.what_to_do[index_what_to_do])
                #return ('c{}'.format(what_to_do))

            elif self.what_to_do[index_what_to_do] <= number_cards and self.latest_turn_memory[0]==0 and game.red_coins<2 : #If the most recent recommendation was to play a card, one card has been played since the hint was given, and the players have made fewer than two errors, play the recommended card
                self.latest_turn_memory[0]+=1
                game.current_hand.cards.append(virtual_card) #on rajoute une carte "virtuelle" pour conserver le même nombre de cartes total (len(visible) = constante)
                return('p%d'%self.what_to_do[index_what_to_do])
                #return ('c{}'.format(what_to_do))
            
            elif game.blue_coins > 0 : #If the players have a hint token, give a hint
                self.latest_turn_memory=[0,0,S]
                if number_cards == 4 :
                    recommendation = self.recommendation_4cards(S)
                else :
                    recommendation = self.recommendation_5cards(S)
                card_to_hint=visible[recommendation[1]*number_cards] #on donne un indice sur la premiere carte du joueur considere
                if recommendation[0]=='number':

                    for j in range(number_players-1):
                        what_to_do_j = self.latest_turn_memory[2]
                        players_not_hinters_j = [i for i in range(number_players-1) if i != j]
                        for i in players_not_hinters_j: #on considère tous les autres joueurs sauf celui qui a donné le dernier indice
                            what_to_do_j -= color_by_players[i]
                        what_to_do_j %= (2*number_cards)
                        what_to_do_j += 1
                        self.what_to_do[j] = what_to_do_j

                    return ('c{}{}'.format(card_to_hint.number,self.list_players[recommendation[1]][0]))
                if recommendation[0]=='color':

                    for j in range(number_players-1):
                        what_to_do_j = self.latest_turn_memory[2]
                        players_not_hinters_j = [i for i in range(number_players-1) if i != j]
                        for i in players_not_hinters_j: #on considère tous les autres joueurs sauf celui qui a donné le dernier indice
                            what_to_do_j -= color_by_players[i]
                        what_to_do_j %= (2*number_cards)
                        what_to_do_j += 1
                        self.what_to_do[j] = what_to_do_j

                    return ('c{}{}'.format(str(card_to_hint.color)[0],self.list_players[recommendation[1]][0]))
                
            elif self.what_to_do[index_what_to_do] > number_cards : #If the most recent recommendation was to discard a card, discard the requested card
                self.latest_turn_memory[1]+=1
                game.current_hand.cards.append(virtual_card) #on rajoute une carte "virtuelle" pour conserver le même nombre de cartes total (len(visible) = constante)
                return('d%d'%(self.what_to_do[index_what_to_do]-number_cards))
                #return ('c{}'.format(what_to_do))
            
            else : #Otherwise, discard c1
                self.latest_turn_memory[1]+=1
                game.current_hand.cards.append(virtual_card) #on rajoute une carte "virtuelle" pour conserver le même nombre de cartes total (len(visible) = constante)
                return('d1')
            ### FIN WHAT TO DO ###            