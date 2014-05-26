#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Game(object):
    def __init__(self, name, *args, **kwargs):
        super(Game, self).__init__(*args, **kwargs)
        self._name = name 

    @property
    def name(self):
        return self._name

    def pre_round(self):
        pass

    def pre_hole(self):
        pass

    def at_turn(self):
        pass

    def post_hole(self):
        pass

    def post_round(self):
        pass

# vim: filetype=python
