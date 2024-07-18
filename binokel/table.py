from typing import List

from pydantic import BaseModel

from binokel.player import Player


class Table(BaseModel):
    players: List[Player]
