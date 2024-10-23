#!/usr/bin/env python


from .tee import Tee
from .tee import TeeMarker


class Hole:
    """
    >>> h = Hole(1, {})
    >>> h.number
    1
    >>> h.tees
    {}
    >>> h.get_tee(1) is None
    True
    >>> str(h)
    'Hole 1'
    """

    def __init__(self, number: int, tees: dict[TeeMarker, Tee]) -> None:
        super().__init__()
        self._number = number
        self._tees = tees or {}

    @property
    def number(self) -> int:
        return self._number

    @property
    def tees(self) -> dict[TeeMarker, Tee]:
        return self._tees

    def get_tee(self, marker: TeeMarker) -> Tee | None:
        return self._tees.get(marker)

    def __str__(self) -> str:
        return f"Hole {self.number}"


# vim: filetype=python
