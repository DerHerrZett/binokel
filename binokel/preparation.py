import random
from binokel import card


def get_shuffled_deck(with_sevens=False):
    cards = []
    for name in card.CardName:
        value = card.CardRank(name=name, value=0)
        for suit in card.CardSuit:
            current_card = card.Card(suit=suit, rank=value).show()
            cards += [current_card, current_card]
    random.shuffle(cards)
    return cards
