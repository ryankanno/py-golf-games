#!/usr/bin/env python

from enum import Enum
from enum import unique


@unique
class Gender(Enum):
    M = 1
    F = 2


class Player:
    """
    >>> p = Player("SpongeBob", Gender.M, 10)
    >>> p.name
    'SpongeBob'
    >>> p.gender.name
    'M'
    >>> p.handicap
    10
    >>> str(p)
    'SpongeBob'
    """

    def __init__(self, name: str, gender: Gender, handicap: int = 0) -> None:
        super().__init__()
        self._name = name
        self._gender = gender
        self._handicap = handicap

    @property
    def name(self) -> str:
        return self._name

    @property
    def gender(self) -> Gender:
        return self._gender

    @property
    def handicap(self) -> int:
        return self._handicap

    def __str__(self) -> str:
        return self._name


# vim: filetype=python
