from binokel import card

for name in card.CardName:
    value = card.CardRank(name=name, value=0)
    for suit in card.CardSuit:
        print(card.Card(suit=suit, rank=value).show())

