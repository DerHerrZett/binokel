from enum import Enum
from pydantic import BaseModel


class CardSuit(str, Enum):
    herz = "\U00002764"
    kreuz = "\U0001F330"
    schellen = "\U0001F9C5"
    schippen = "\U0001F340"


class CardRank(str, Enum):
    ass = "A"
    zehn = "10"
    koenig = "K"
    ober = "O"
    unter = "U"
    sieben = "7"


card_value_map = {"A": 11, "10": 10, "K": 4, "O": 3, "U": 2, "7": 0}


class Card(BaseModel):
    suit: CardSuit
    rank: CardRank
    value: int = 0

    def model_post_init(self, ctx):
        self.value = card_value_map[self.rank.value]

    def show(self, verbose=False) -> str:
        out_string = f"{self.suit.value}{self.rank.value}"
        if verbose:
            out_string = f"{out_string}[{self.value}]"
        return out_string
