#!/usr/bin/env python

import typing

from .player import Player


class HoleScore:
    """
    >>> score = HoleScore(1, 4)
    >>> score.hole_number
    1
    >>> score.hole_number = 2
    >>> score.hole_number
    2
    >>> score.score
    4
    >>> score.score = 10
    >>> score.score
    10
    """

    def __init__(self, hole_number: int, score: int) -> None:
        super().__init__()
        self.hole_number = hole_number
        self.score = score

    @property
    def hole_number(self) -> int:
        return self._hole_number

    @hole_number.setter
    def hole_number(self, value: int) -> None:
        self._hole_number = value

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, value: int) -> None:
        self._score = value


class PlayerScores:
    """
    >>> from .player import Gender, Player
    >>> p = Player("SpongeBob", Gender.M, 10)
    >>> ps = PlayerScores(p)
    >>> ps.record_score(1, 5)
    >>> ps.record_score(2, 3)
    >>> ps.total_score
    8
    >>> hole_score = ps.get_score(1)
    >>> hole_score.hole_number
    1
    >>> hole_score.score
    5
    """

    def __init__(self, player: Player) -> None:
        super().__init__()
        self._player = player
        self._hole_scores: dict[int, HoleScore] = {}

    def record_score(self, hole_number: int, score: int) -> None:
        self._hole_scores[hole_number] = HoleScore(hole_number, score)

    def get_score(self, hole_number: int) -> HoleScore | None:
        return self._hole_scores.get(hole_number, None)

    @property
    def total_score(self) -> int:
        return sum(
            hole_score.score for hole_score in self._hole_scores.values()
        )

    def __iter__(self) -> typing.Iterator[HoleScore]:
        return iter(self._hole_scores.values())


class Scorecard:
    """
    >>> from .player import Gender, Player
    >>> p1 = Player("SpongeBob", Gender.M, 10)
    >>> p2 = Player("Squarepants", Gender.F, 10)
    >>> scorecard = Scorecard()
    >>> scorecard.record_score(p1, 1, 5)
    >>> scorecard.record_score(p2, 1, 3)
    >>> scorecard.get_scores(p1) #doctest: +ELLIPSIS
    <py_golf_games.scorecard.PlayerScores object at 0x...>
    >>> scorecard.get_score(p1, 1).score
    5
    >>> scorecard.get_score(p2, 1).score
    3
    """

    def __init__(self) -> None:
        super().__init__()
        self._player_scores: dict[Player, PlayerScores] = {}

    def record_score(
        self, player: Player, hole_number: int, score: int
    ) -> None:
        if player not in self._player_scores:
            self._player_scores[player] = PlayerScores(player)

        self._player_scores[player].record_score(hole_number, score)

    def get_scores(self, player: Player) -> PlayerScores | None:
        return self._player_scores.get(player, None)

    def get_score(self, player: Player, hole_number: int) -> HoleScore | None:
        return (
            self._player_scores[player].get_score(hole_number)
            if player in self._player_scores
            else None
        )


# vim: filetype=python
