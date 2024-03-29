#!/usr/bin/env python

import typing

from ..player import Player
from .game import Game


class Stroke(Game):
    def __init__(self, players: typing.List[Player]) -> None:
        super().__init__("Stroke", players)


# vim: filetype=python
