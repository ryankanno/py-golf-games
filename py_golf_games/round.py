#!/usr/bin/env python


from .course import Course
from .player import Player
from .scorecard import Scorecard


class Round:
    """
    >>> from .player import Gender, Player
    >>> p1 = Player("SpongeBob", Gender.M, 10)
    >>> p2 = Player("Squarepants", Gender.F, 10)
    >>> from .course import Course
    >>> course = Course("Ocean")
    >>> golf_round = Round(course, [p1, p2])
    >>> course is golf_round.course
    True
    >>> len(golf_round.players)
    2
    >>> p3 = Player("Joe", Gender.M, 10)
    >>> golf_round.add_player(p3)
    >>> len(golf_round.players)
    3
    >>> from .scorecard import Scorecard
    >>> x = golf_round.scorecard
    >>> type(x) is Scorecard
    True
    >>> golf_round.current_hole is None
    True
    >>> golf_round.start()
    >>> golf_round.current_hole
    1
    >>> golf_round.advance_hole()
    >>> golf_round.current_hole
    2
    """

    def __init__(self, course: Course, players: list[Player]) -> None:
        super().__init__()
        self._course = course
        self._players = players
        self._scorecard = Scorecard()
        self._current_hole: int | None = None

    @property
    def course(self) -> Course:
        return self._course

    @property
    def players(self) -> list[Player]:
        return self._players

    @property
    def scorecard(self) -> Scorecard:
        return self._scorecard

    @property
    def current_hole(self) -> int | None:
        return self._current_hole

    @current_hole.setter
    def current_hole(self, value: int | None) -> None:
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
