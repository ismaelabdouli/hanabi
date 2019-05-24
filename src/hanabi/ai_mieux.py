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

class Player_better(AI):

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

        ####### CLUE SI POSSIBLE
        
        #le meilleur coup est de donner un indice utile, si possible(assez de jetons)
        if game.blue_coins > 0:
            number_players=len(game.players)
            visible = [card for card in self.other_players_cards]


        
            ######### SAVE CLUE

            #On commence par regarder les chop cards
            chop_cards = [ (visible[0+i*game.deck.cards_by_player[number_players]],i*game.deck.cards_by_player[number_players]) for i in range(number_players-1)]
            not_chop_cards = [(visible[i],i) for i in range(len(visible)) if i%game.deck.cards_by_player[number_players]!=0]
            for (card,ind) in chop_cards:
                left_cards = [visible[i] for i in range(len(visible)) if i!=ind]

                #Si on trouve un cinq on donne un save clue de nombre directement
                if card.number == 5 and card.number_clue == False:
                    #print("I give a clue!")
                    return("c%s"%5)

                #A AMELIORER : Si on trouve un deux on donne un save clue de nombre (corriger apr�s pour donner un indice que si c'est int�ressant)
                if card.number == 2 and card.number_clue == False:    
                    if card not in left_cards : #on rentre dans ce if si la carte n'est nulle part ailleurs(on n'oublie pas de ne pas recompter la carte que l'on consid�re)
                        if card.number>game.piles[card.color]: #on rentre si la carte n'a pas �t� encore pos�e
                            #print("I give a clue!")
                            return("c%s"%2)
                            #Si on trouve une derni�re carte en jeu, on donne un save clue si on peut encore donner un indice
                
                count=0
                for card_from_discard in game.discard_pile.cards:
                    if card_from_discard == card:
                        count += 1 
                if (count == game.deck.card_count[card.number]-1): #si oui, alors c'est la derni�re carte, qui n'a obligatoirement pas �t� jou�e car toutes les autres sont dans la pile
                    #si pas d'indice de nombre, on donne un indice de nombre
                    if card.number_clue == False:
                        #print("I give a clue")
                        return("c%s"%card.number)
                    
                    #si pas d'indice de couleur, on donne un indice de couleur
                    elif card.color_clue == False:
                        #print("I give a clue")
                        c = "c%s"%card.color
                        return(c[:2])
                        
                #On donne un indice si la carte en question n'est visible nulle part ailleurs (mains ou piles de jeu)
                if card not in left_cards: #on rentre dans ce if si la carte n'est nulle part ailleurs(on n'oublie pas de ne pas recompter la carte que l'on consid�re)
                    if card.number > game.piles[card.color]: #on rentre si la carte n'a pas �t� encore pos�e
                
                        #si pas d'indice de nombre, on donne un indice de nombre
                        if card.number_clue == False:
                            #print("I give a clue")
                            return("c%s"%card.number)
                    
                        #si pas d'indice de couleur, on donne un indice de couleur
                        elif card.color_clue == False:
                            #print("I give a clue")
                            c = "c%s"%card.color
                            return(c[:2])

                ####### PLAY CLUE    
                #Si la carte est jouable ,on donne un play clue de nombre si pas encore d'indice correspondant
                if game.piles[card.color]+1 == card.number:
                    #si pas d'indice de nombre, on donne un indice de nombre
                    if card.number_clue == False:
                        #print("I give a clue")
                        return("c%s"%card.number)
                    
                    #si pas d'indice de couleur, on donne un indice de couleur
                    elif card.color_clue == False:
                        #print("I give a clue")
                        c = "c%s"%card.color
                        return(c[:2])

            #On regarde maintenant les autres cartes dans l'ordre de gauche à droite
            for (card,ind) in not_chop_cards:
                left_cards =  [visible[i] for i in range(len(visible)) if i!=ind]

                #Si on trouve un cinq on donne un save clue de nombre directement
                if card.number == 5 and card.number_clue == False:
                    #print("I give a clue!")
                    return("c%s"%5)

                #A AMELIORER : Si on trouve un deux on donne un save clue de nombre (corriger apr�s pour donner un indice que si c'est int�ressant)                    if card.number == 2 and card.number_clue == False:
                if card.number == 2 and card.number_clue == False:
                    if card not in left_cards: #on rentre dans ce if si la carte n'est nulle part ailleurs(on n'oublie pas de ne pas recompter la carte que l'on consid�re)
                        if card.number>game.piles[card.color]: #on rentre si la carte n'a pas �t� encore pos�e
                            #print("I give a clue!")
                            return("c%s"%2)
                            #Si on trouve une derni�re carte en jeu, on donne un save clue si on peut encore donner un indice
                
                count=0
                for card_from_discard in game.discard_pile.cards:
                    if card_from_discard == card:
                        count += 1 
                if (count == game.deck.card_count[card.number]-1): #si oui, alors c'est la derni�re carte, qui n'a obligatoirement pas �t� jou�e car toutes les autres sont dans la pile                        #si pas d'indice de nombre, on donne un indice de nombre
                    if card.number_clue == False:
                        #print("I give a clue")
                        return("c%s"%card.number)
                    
                    #si pas d'indice de couleur, on donne un indice de couleur
                    elif card.color_clue == False:
                        #print("I give a clue")
                        c = "c%s"%card.color
                        return(c[:2])
                        
                #On donne un indice si la carte en question n'est visible nulle part ailleurs (mains ou piles de jeu)
                if card not in left_cards: #on rentre dans ce if si la carte n'est nulle part ailleurs(on n'oublie pas de ne pas recompter la carte que l'on consid�re)
                    if card.number > game.piles[card.color]: #on rentre si la carte n'a pas �t� encore pos�e
                
                        #si pas d'indice de nombre, on donne un indice de nombre
                        if card.number_clue == False:
                            #print("I give a clue")
                            return("c%s"%card.number)
                    
                        #si pas d'indice de couleur, on donne un indice de couleur
                        elif card.color_clue == False:
                            #print("I give a clue")
                            c = "c%s"%card.color
                            return(c[:2])

                ####### PLAY CLUE    
                #Si la carte est jouable ,on donne un play clue de nombre si pas encore d'indice correspondant
                if game.piles[card.color]+1 == card.number:
                    #si pas d'indice de nombre, on donne un indice de nombre
                    if card.number_clue == False:
                        #print("I give a clue")
                        return("c%s"%card.number)
                    
                #si pas d'indice de couleur, on donne un indice de couleur
                elif card.color_clue == False:
                    #print("I give a clue")
                    c = "c%s"%card.color
                    return(c[:2])


                    
            

                        
                        
                        
        ####### CLUE PAS INTERESSANT DONC PLAY
        #A AMELIORER : On ne joue une carte que si on est s�r de pouvoir la jouer (On peut essayer de jouer d'autres cartes dont on peut peut �tre deviner la jouabilit� d'apr�s notre strat�gie)
        
        playable = [ (i+1, card) for (i,card) in
                     enumerate(game.current_hand.cards)
                     if (card.color_clue != False and card.number_clue != False and game.piles[card.color]+1 == card.number) ] #on peut jouer une carte si on a tous les indices dessus et qu'elle est effectivement jouable en regardant la pile


        if playable:
            # sort by ascending number, then newest
            playable.sort(key=lambda p: (p[1].number, -p[0]))
            #print ('AI_Better would play:', "p%d"%playable[0][0], end=' ')
            #if (len(playable)>1):
                #print('but could also pick:', playable[1:])

            return "p%d"%playable[0][0]
            
            
        
            
        ####### IL NE RESTE QUE DISCARD
        #On discard la carte non indic�e la plus � droite, la "CHOP" card
        hand = [ (i+1, card) for (i,card) in enumerate(game.current_hand.cards)]
        card_to_discard = "Empty"
        for (i,card_maybe_discardable) in reversed(hand):
            if (card_maybe_discardable.color_clue != False and card_maybe_discardable.number_clue != False):
                card_to_discard = card_maybe_discardable
                discardable=i
                #on conserve la carte(son rang) sans indice la plus � droite en parcourant la main de gauche � droite et en gardant la derni�re carte qui convient
        
        if card_to_discard != "Empty": #on a alors trouv� une carte sans indice que l'on discard
            #print("I discard!")
            return "d%d"%discardable
        
        #Sinon on prend la chop card en regardant que les indices nombres        
        for (i,card_maybe_discardable) in reversed(hand):
            if (card_maybe_discardable.number_clue != False):
                card_to_discard = card_maybe_discardable
                discardable=i
                #on conserve la carte(son rang) sans indice la plus � droite en parcourant la main de gauche � droite et en gardant la derni�re carte qui convient
        
        if card_to_discard != "Empty": #on a alors trouv� une carte sans indice de nombre que l'on discard
                #print("I discard!")
                return "d%d"%discardable
                
        #Sinon on prend la chop card en regardant que les indices couleurs        
        for (i,card_maybe_discardable) in reversed(hand):
            if (card_maybe_discardable.color_clue != False):
                card_to_discard = card_maybe_discardable
                discardable=i
                #on conserve la carte(son rang) sans indice la plus � droite en parcourant la main de gauche � droite et en gardant la derni�re carte qui convient
        
        if card_to_discard != "Empty": #on a alors trouv� une carte sans indice de nombre que l'on discard
                #print("I discard!")
                return "d%d"%discardable
                
        #Sinon on jette la premi�re carte pour �tre s�r de faire quelque chose (normalement on n'arrive pas ici)
        #print("I discard!")
        return "d%d"%1 