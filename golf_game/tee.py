#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum
from enum import unique


@unique
class TeeMarker(Enum):
    Gold = 1
    Blue = 2
    White = 3
    Red = 4
    Green = 5


class Tee(object):
    """
    """
    def __init__(self, marker, par, distance, handicap=None, *args, **kwargs):
        super(Tee, self).__init__(*args, **kwargs)
        self._marker = marker
        self._par = par
        self._distance = distance
        self._handicap = handicap
        assert self._marker in list(TeeMarker)

    @property
    def par(self):
        return self._par

    @property
    def marker(self):
        return self._marker

    @property
    def distance(self):
        return self._distance

    @property
    def handicap(self):
        return self._handicap

    def __str__(self):
        return self.name

# vim: filetype=python
