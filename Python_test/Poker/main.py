from Poker.Card import Card
from Poker.Deck import Deck

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

#mala practica: doble punto de métodos.
#deck.cards.extend(cards)
print(cards)