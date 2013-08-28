#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scorecard import Scorecard

class Round(object):
    def __init__(self, course, players=[], *args, **kwargs):
        super(Round, self).__init__(*args, **kwargs)
        self._course = course
        self._players = players 
        self._scorecard = Scorecard()

    @property
    def course(self):
        return self._course

    @property
    def scorecard(self):
        return self._scorecard

    def add_player(self, player):
        self._players.push(player)

    def record_score(self, hole_number, player, score):
        print "GOING TO"
        if player in self._players and self.course.get_hole(hole_number):
            print "RECORDING"
            self.scorecard.record_score(hole_number, player, score)


# vim: filetype=python
