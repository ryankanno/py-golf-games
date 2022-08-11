#!/usr/bin/env python
# -*- coding: utf-8 -*-

import typing

from ..players import Player
from .game import Game


class Stroke(Game):
    def __init__(self, players: typing.List[Player]) -> None:
        super().__init__("Stroke", players)


# vim: filetype=python
