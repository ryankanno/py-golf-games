#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Hole(object):
    """
    >>> h = Hole(1, 4, 500)
    >>> h.number
    1
    >>> h.distance
    500
    >>> h.par
    4
    """
    def __init__(self, number, par, distance, *args, **kwargs):
        super(Hole, self).__init__(*args, **kwargs)
        self._number = number
        self._par = par
        self._distance = distance

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value

    @property
    def par(self):
        return self._par

    @par.setter
    def par(self, value):
        self._par = value

    def __str__(self):
        return "Hole {0} (par {1}, {2} yards)".format(
            self.number, self.par, self.distance)

# vim: filetype=python
