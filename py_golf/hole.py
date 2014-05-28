#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Hole(object):
    """
    >>> h = Hole(1, {})
    >>> h.number
    1
    >>> h.tees
    {}
    >>> h.get_tee(1) is None
    True
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
        try:
            return self._tees[marker]
        except:
            return None

    def __str__(self):
        return "Hole {0} (par {1})".format(
            self.number, self.par)

# vim: filetype=python
