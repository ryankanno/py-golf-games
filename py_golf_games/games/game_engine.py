#!/usr/bin/env python

import typing

from ..player import Player
from ..round import Round
from .game import Game


class GameEngine:
    def __init__(self, round: Round):
        super().__init__()
        self._round = round
        self._games: typing.List[Game] = []

    def enable_game(self, player: Player, game: Game) -> None:
        self._games.append(game)


# vim: filetype=python
