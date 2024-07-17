from enum import Enum
from pydantic import BaseModel


class Suit(Enum):
    herz = "Herz"
    kreuz = "Kreuz"
    schellen = "Schellen"
    schippen = "Schippen"

class Name(Enum):
    ass = "Ass"
    zehn = "10"
    koenig = "Koenig"
    ober = "Ober"
    unter = "Unter"
    sieben = "7"

class Value(BaseModel):
    name:Name
    points: int

class Card(BaseModel):
    suit: Suit
    value: Value

    def show(self) -> str:
        return f"{self.suit} {self.value.name}"

