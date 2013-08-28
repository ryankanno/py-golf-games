#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PlayerScores(object):
    def __init__(self, player, *args, **kwargs):
        super(PlayerScores, self).__init__(*args, **kwargs)
        self._player = player
        self._hole_scores = {}

    def record_score(self, hole_number, score):
        self._hole_scores[hole_number] = HoleScore(hole_number, score)

    def get_score(self, hole_number):
        return self._hole_scores[hole_number] if hole_number in self._hole_scores else None

    def __iter__(self):
        return iter(self._hole_scores)


class HoleScore(object):
    def __init__(self, hole_number, score, *args, **kwargs):
        super(HoleScore, self).__init__(*args, **kwargs)
        self._hole_number = hole_number
        self.score = score 

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


class Scorecard(object):
    def __init__(self, *args, **kwargs):
        super(Scorecard, self).__init__(*args, **kwargs)
        self._player_scores = {}

    def record_score(self, player, hole_number, score):
        print "in"
        if player not in self._player_scores:
            print "Not in"
            self._player_scores[player] = PlayerScores(player)

        self._player_scores[player].record_score(hole_number, score) 

    def get_scores(self, player):
        return self._player_scores[player] if player in self._player_scores \
            else None

    def get_score(self, player, hole_number):
        return self._player_scores[player].get_score(hole_number) \
            if player in self._player_scores else None


# vim: filetype=python
