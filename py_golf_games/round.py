#!/usr/bin/env python
# -*- coding: utf-8 -*-

import typing

from .course import Course
from .player import Player
from .scorecard import Scorecard


class Round(object):
    """
    >>> from .player import Gender, Player
    >>> p1 = Player("SpongeBob", Gender.M, 10)
    >>> p2 = Player("Squarepants", Gender.F, 10)
    >>> from .course import Course
    >>> course = Course("Ocean")
    >>> round = Round(course, [p1, p2])
    >>> course is round.course
    True
    >>> len(round.players)
    2
    >>> p3 = Player("Joe", Gender.M, 10)
    >>> round.add_player(p3)
    >>> len(round.players)
    3
    >>> from .scorecard import Scorecard
    >>> x = round.scorecard
    >>> type(x) is Scorecard
    True
    >>> round.current_hole is None
    True
    >>> round.start()
    >>> round.current_hole
    1
    >>> round.advance_hole()
    >>> round.current_hole
    2
    """

    def __init__(self, course: Course, players: typing.List[Player]) -> None:
        super(Round, self).__init__()
        self._course = course
        self._players = players
        self._scorecard = Scorecard()
        self._current_hole: typing.Optional[int] = None

    @property
    def course(self) -> Course:
        return self._course

    @property
    def players(self) -> typing.List[Player]:
        return self._players

    @property
    def scorecard(self) -> Scorecard:
        return self._scorecard

    @property
    def current_hole(self) -> typing.Optional[int]:
        return self._current_hole

    @current_hole.setter
    def current_hole(self, value: typing.Optional[int]) -> None:
        self._current_hole = value

    def add_player(self, player: Player) -> None:
        self._players.append(player)

    def record_score(
        self, player: Player, hole_number: int, score: int
    ) -> None:
        if player in self._players and self.course.get_hole(hole_number):
            self.scorecard.record_score(player, hole_number, score)

    def start(self) -> None:
        self.current_hole = 1

    def advance_hole(self) -> None:
        if self.current_hole is not None:
            self.current_hole += 1


# vim: filetype=python
