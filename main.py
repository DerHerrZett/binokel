from binokel import card

for name in card.Name:
    value = card.Value(name=name, points=0)
    for suit in card.Suit:
        print(card.Card(suit=suit, value=value).show())

