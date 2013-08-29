#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Player(object):
    def __init__(self, name, handicap=0, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        self._name = name
        self._handicap = handicap

    @property
    def name(self):
        return self._name

    @property
    def handicap(self):
        return self._handicap

    def __str__(self):
        return self._name

# vim: filetype=python
