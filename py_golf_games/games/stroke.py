#!/usr/bin/env python


from ..player import Player
from .game import Game


class Stroke(Game):
    def __init__(self, players: list[Player]) -> None:
        super().__init__("Stroke", players)


# vim: filetype=python
