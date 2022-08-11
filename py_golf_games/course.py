#!/usr/bin/env python
# -*- coding: utf-8 -*-

import typing

from .hole import Hole
from .tee import TeeMarker


class Course(object):
    """
    >>> from .hole import Hole
    >>> from .tee import TeeMarker, Tee
    >>> c = Course("Hawaii Kai")
    >>> c.name
    'Hawaii Kai'
    >>> t1 = Tee(TeeMarker.Gold, 5, 600, 1)
    >>> t2 = Tee(TeeMarker.Gold, 3, 300, 2)
    >>> h1 = Hole(1, {TeeMarker.Gold: t1})
    >>> h2 = Hole(2, {TeeMarker.Gold: t2})
    >>> c.add_hole(1, h1)
    >>> c.add_hole(2, h2)
    >>> c.total_distance(TeeMarker.Gold)
    900
    >>> c.total_par(TeeMarker.Gold)
    8
    >>> len(c.holes)
    2
    >>> str(c)
    'Hawaii Kai'
    >>> h1 is c.get_hole(1)
    True
    """

    def __init__(self, name: str):
        super(Course, self).__init__()
        self._name = name
        self._holes: typing.Dict[int, Hole] = {}

    def add_hole(self, hole_number: int, hole: Hole) -> None:
        self._holes[hole_number] = hole

    def get_hole(self, hole_number: int) -> typing.Optional[Hole]:
        return self._holes[hole_number] if hole_number in self._holes else None

    @property
    def holes(self) -> typing.ValuesView[Hole]:
        return self._holes.values()

    @property
    def name(self) -> str:
        return self._name

    def total_distance(self, tee_marker: TeeMarker) -> int:
        total_distance = 0
        for hole in self.holes:
            tee = hole.get_tee(tee_marker)
            total_distance += tee.distance if tee else 0
        return total_distance

    def total_par(self, tee_marker: TeeMarker) -> int:
        total_par = 0
        for hole in self.holes:
            tee = hole.get_tee(tee_marker)
            total_par += tee.par if tee else 0
        return total_par

    def __str__(self) -> str:
        return self.name


# vim: filetype=python
