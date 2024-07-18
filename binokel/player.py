from typing import List

from pydantic import BaseModel

from binokel.card import Card


class Player(BaseModel):
    cards: List[Card]
    auction_points: int
    meld_points: int
    trick_points: int
