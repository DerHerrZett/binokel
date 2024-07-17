from enum import Enum
from pydantic import BaseModel


class CardSuit(Enum):
    herz = "Herz"
    kreuz = "Kreuz"
    schellen = "Schellen"
    schippen = "Schippen"

class CardName(Enum):
    ass = "Ass"
    zehn = "10"
    koenig = "Koenig"
    ober = "Ober"
    unter = "Unter"
    sieben = "7"

class CardRank(BaseModel):
    name:CardName
    value: int

class Card(BaseModel):
    suit: CardSuit
    rank: CardRank

    def show(self) -> str:
        return f"{self.suit.value} {self.rank.name.value}"

