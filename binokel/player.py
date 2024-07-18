from typing import Optional, List

from pydantic import BaseModel

from binokel.card import Card


class Player(BaseModel):
    name: str
    cards: Optional[List[Card]] = []
    auction_points: int = 0
    meld_points: int = 0
    trick_points: int = 0
    total_score: int = 0

    def show_cards(self):
        stringlist = [card.show() for card in self.cards]
        print(" ".join(stringlist))
