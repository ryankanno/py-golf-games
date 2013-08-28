#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scorecard import Scorecard
from game_engine import GameEngine

class Round(object):
    def __init__(self, course, players=[], *args, **kwargs):
        super(Round, self).__init__(*args, **kwargs)
        self._course = course
        self._players = players 
        self._scorecard = Scorecard()
        self._game_engine = GameEngine()

    @property
    def course(self):
        return self._course

    @property
    def players(self):
        return self._players

    @property
    def scorecard(self):
        return self._scorecard

    def add_player(self, player):
        self._players.push(player)

    def record_score(self, player, hole_number, score):
        if player in self._players and self.course.get_hole(hole_number):
            self.scorecard.record_score(player, hole_number, score)


# vim: filetype=python
