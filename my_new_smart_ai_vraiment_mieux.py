import hanabi.ai

class Player_better(hanabi.ai.AI):

    def play(self):
        game = self.game
        ####### CLUE SI POSSIBLE
        
        #le meilleur coup est de donner un indice utile, si possible(assez de jetons)
        if game.blue_coins > 0:
            list_hands= [ (i+1,card) for (i,card) in enumerate(game.hands[game.other_player].cards)]
            
            #On regarde la main des autres joueurs pour trouver un indice � donner
            #A AMELIORER : faire un modulo cinq pour d'abord regarder que les chop
            L=[list_hands[len(list_hands)-1]]
            L+=list_hands[0:len(list_hands)-1]
            for (ind,card) in L:
            
            ######### SAVE CLUE
                #Si on trouve un cinq on donne un save clue de nombre directement
                if card.number == 5 and card.number_clue == False:
                    print("I give a clue!")
                    return("c%s"%5)
                    
                #A AMELIORER : Si on trouve un deux on donne un save clue de nombre (corriger apr�s pour donner un indice que si c'est int�ressant)
                if card.number == 2 and card.number_clue == False:
                    for other_hands_card in list_hands:
                        if (card!=other_hands_card[1] and ind!=list_hands[0]): #on rentre dans ce if si la carte n'est nulle part ailleurs(on n'oublie pas de ne pas recompter la carte que l'on consid�re)
                            if card.number>game.piles[card.color]: #on rentre si la carte n'a pas �t� encore pos�e
                                print("I give a clue!")
                                return("c%s"%2)
                
                #Si on trouve une derni�re carte en jeu, on donne un save clue si on peut encore donner un indice
                count=0
                for card_from_discard in game.discard_pile.cards:
                    if card_from_discard == card:
                        count += 1 
                if (count == game.deck.card_count[card.number]-1): #si oui, alors c'est la derni�re carte, qui n'a obligatoirement pas �t� jou�e car toutes les autres sont dans la pile
                    #si pas d'indice de nombre, on donne un indice de nombre
                    if card.number_clue == False:
                        print("I give a clue")
                        return("c%s"%card.number)
                    
                    #si pas d'indice de couleur, on donne un indice de couleur
                    elif card.color_clue == False:
                        print("I give a clue")
                        return("c%s"%card.color)
                        
                #On donne un indice si la carte en question n'est visible nulle part ailleurs (mains ou piles de jeu)
                for other_hands_card in list_hands:
                    if (card!=other_hands_card[1] and ind!=list_hands[0]): #on rentre dans ce if si la carte n'est nulle part ailleurs(on n'oublie pas de ne pas recompter la carte que l'on consid�re)
                        if card.number > game.piles[card.color]: #on rentre si la carte n'a pas �t� encore pos�e
                    
                            #si pas d'indice de nombre, on donne un indice de nombre
                            if card.number_clue == False:
                                print("I give a clue")
                                return("c%s"%card.number)
                    
                            #si pas d'indice de couleur, on donne un indice de couleur
                            elif card.color_clue == False:
                                print("I give a clue")
                                return("c%s"%card.color)
                    
            
            ####### PLAY CLUE    
                #Si la carte est jouable ,on donne un play clue de nombre si pas encore d'indice correspondant
                if game.piles[card.color]+1 == card.number:
                    #si pas d'indice de nombre, on donne un indice de nombre
                    if card.number_clue == False:
                        print("I give a clue")
                        return("c%s"%card.number)
                    
                    #si pas d'indice de couleur, on donne un indice de couleur
                    elif card.color_clue == False:
                        print("I give a clue")
                        return("c%s"%card.color)
                        
                        
                        
        ####### CLUE PAS INTERESSANT DONC PLAY
        #A AMELIORER : On ne joue une carte que si on est s�r de pouvoir la jouer (On peut essayer de jouer d'autres cartes dont on peut peut �tre deviner la jouabilit� d'apr�s notre strat�gie)
        
        playable = [ (i+1, card) for (i,card) in
                     enumerate(game.current_hand.cards)
                     if (card.color_clue != False and card.number_clue != False and game.piles[card.color]+1 == card.number) ] #on peut jouer une carte si on a tous les indices dessus et qu'elle est effectivement jouable en regardant la pile

        if playable:
            # sort by ascending number, then newest
            playable.sort(key=lambda p: (p[1], -p[0]))
            print ('AI_Better would play:', "p%d"%playable[0][0], end=' ')
            if (len(playable)>1):
                print('but could also pick:', playable[1:])
            else: print()

            return "p%d"%playable[0][0]
            
            
        
            
        ####### IL NE RESTE QUE DISCARD
        #On discard la carte non indic�e la plus � droite, la "CHOP" card
        hand = [ (i+1, card) for (i,card) in enumerate(game.current_hand.cards)]
        card_to_discard = "Empty"
        for (i,card_maybe_discardable) in hand:
            if (card_maybe_discardable.color_clue != False and card_maybe_discardable.number_clue != False):
                card_to_discard = card_maybe_discardable
                discardable=i
                #on conserve la carte(son rang) sans indice la plus � droite en parcourant la main de gauche � droite et en gardant la derni�re carte qui convient
        
        if card_to_discard != "Empty": #on a alors trouv� une carte sans indice que l'on discard
            print("I discard!")
            return "d%d"%discardable
        
        #Sinon on prend la chop card en regardant que les indices nombres        
        for (i,card_maybe_discardable) in hand:
            if (card_maybe_discardable.number_clue != False):
                card_to_discard = card_maybe_discardable
                discardable=i
                #on conserve la carte(son rang) sans indice la plus � droite en parcourant la main de gauche � droite et en gardant la derni�re carte qui convient
        
        if card_to_discard != "Empty": #on a alors trouv� une carte sans indice de nombre que l'on discard
                print("I discard!")
                return "d%d"%discardable
                
        #Sinon on prend la chop card en regardant que les indices couleurs        
        for (i,card_maybe_discardable) in hand:
            if (card_maybe_discardable.color_clue != False):
                card_to_discard = card_maybe_discardable
                discardable=i
                #on conserve la carte(son rang) sans indice la plus � droite en parcourant la main de gauche � droite et en gardant la derni�re carte qui convient
        
        if card_to_discard != "Empty": #on a alors trouv� une carte sans indice de nombre que l'on discard
                print("I discard!")
                return "d%d"%discardable
                
        #Sinon on jette la premi�re carte pour �tre s�r de faire quelque chose (normalement on n'arrive pas ici)
        print("I discard!")
        return "d%d"%1                    
                    
