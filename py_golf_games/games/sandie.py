#!/usr/bin/env python
# -*- coding: utf-8 -*-

import typing

from ..player import Player
from .game import Game


class Sandie(Game):
    def __init__(self, players: typing.List[Player]) -> None:
        super().__init__("Sandie", players)


# vim: filetype=python
