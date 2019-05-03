import unittest
import hanabi



class ColorTest(unittest.TestCase):
    def test_1(self):
        pass


class CardTest(unittest.TestCase):
    def test_1(self):
        pass


class HandTest(unittest.TestCase):
    # test __special__ functions
    

    # test normal functions
    pass

class DeckTest(unittest.TestCase):
    # test __special__ functions
    

    # test normal functions
    def test_shuffle(self):
        self.deck_init = hanabi.deck.Deck()
        self.deck_init.shuffle()
        self.deck_init_2=hanabi.deck.Deck()
        self.assertNotEqual(deck_init,deck_init_2)
        #On vérifie qu'on obtient bien un paquet différent.
        self.assertEqual(len(deck_init.cards),len(deck_init_2.cards))
        #On vérifie que le nombre de cartes est resté identique.

    def test_draw(self):
        self.deck_init = self.hanabi.deck.Deck()
        card=deck_init.cards[0]
        card2=deck_init.draw()
        self.assertEqual(len(deck_init.cards)-1,len(hanabi.deck.cards))
        #On vérifie que la carte piochée a bien été retirée de la pioche.
        self.assertEqual(card,card2)
        #On vérifie que la carte piochée est bien celle qui était en haut du paquet.

    def test_deal(self):
        for nhands in range(2,6):
            self.deck_init=hanabi.deck.Deck()
            self. deck_init.deal(nhands)
            self.assertEqual(len(deck_init.cards),len(hanabi.deck.cards)-nhands*deck_init.cards_by_player[nhands])
            #On vérifie que le bon nombre de cartes a été distribué, et que celles-ci ont bien été retirées de la pîoche.



class GameTest(unittest.TestCase):

    def setUp(self):
        self.unshuffled_game = hanabi.Game()
        self.random_game = hanabi.Game()
        # ... group G here! 
        self.predefined_game = hanabi.Game()
        # ...


    # lines 193, 227
    def test_A1(self):
        pass

    # lines 227, 261
    def test_B1(self):
        pass


    # lines 261, 295


    # lines 295, 329


    # lines 329, 363


    # lines 363, 397


    # lines 397, 431


    pass



if __name__ == '__main__':
    unittest.main()
