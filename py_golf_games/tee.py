#!/usr/bin/env python

import typing
from enum import Enum
from enum import unique


@unique
class TeeMarker(Enum):
    Gold = 1
    Blue = 2
    White = 3
    Red = 4
    Green = 5


class Tee:
    """
    >>> t = Tee(TeeMarker.White, 3, 310, 8)
    >>> t.par
    3
    >>> t.distance
    310
    >>> t.marker.name
    'White'
    >>> t.handicap
    8
    """

    def __init__(
        self,
        marker: TeeMarker,
        par: int,
        distance: int,
        handicap: typing.Optional[int] = None,
    ) -> None:
        super().__init__()
        self._marker = marker
        self._par = par
        self._distance = distance
        self._handicap = handicap

    @property
    def par(self) -> int:
        return self._par

    @property
    def marker(self) -> TeeMarker:
        return self._marker

    @property
    def distance(self) -> int:
        return self._distance

    @property
    def handicap(self) -> typing.Optional[int]:
        return self._handicap


# vim: filetype=python
