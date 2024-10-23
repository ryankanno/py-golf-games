#!/usr/bin/env python


from ..player import Player
from .game import Game


class Sandie(Game):
    def __init__(self, players: list[Player]) -> None:
        super().__init__("Sandie", players)


# vim: filetype=python
