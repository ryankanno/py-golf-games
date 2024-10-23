#!/usr/bin/env python

import typing

from ..player import Player
from ..round import Round
from .game import Game


class GameEngine:
    def __init__(self, golf_round: Round) -> None:
        super().__init__()
        self._round = golf_round
        self._games: typing.List[Game] = []

    def enable_game(self, _player: Player, game: Game) -> None:
        self._games.append(game)


# vim: filetype=python
