#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Hole(object):
    """
    >>> h = Hole(1)
    """
    def __init__(self, number, tees, *args, **kwargs):
        super(Hole, self).__init__(*args, **kwargs)
        self._number = number
        self._tees = tees or {}

    @property
    def number(self):
        return self._number

    @property
    def tees(self):
        return self._tees

    def get_tee(self, marker):
        return self._tees[marker]

    def __str__(self):
        return "Hole {0} (par {1})".format(
            self.number, self.par)

# vim: filetype=python
