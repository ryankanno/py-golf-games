#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
import typing

from ..players import Player


class Game(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, name: str, players: typing.List[Player]) -> None:
        super(Game, self).__init__()
        self._name = name
        self._players = {}
        for player in players:
            self._players[player] = player

    @property
    def name(self) -> str:
        return self._name

    @property
    def players(self) -> typing.ValuesView[Player]:
        return self._players.values()

    def is_participating(self, player: Player) -> bool:
        return player in self._players.values()

    @abc.abstractmethod
    def pre_round(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def pre_hole(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def at_turn(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def post_hole(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def post_round(self) -> None:
        raise NotImplementedError


# vim: filetype=python
