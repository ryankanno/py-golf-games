#!/usr/bin/env python
# -*- coding: utf-8 -*-

from course import Course
from hole import Hole
from player import Player

import random

class CourseGenerator(object):
    @classmethod
    def generate(cls, name, num_holes):
        course = Course(name)
        for hole_number in xrange(1, num_holes + 1):
            hole = HoleGenerator.generate(hole_number)
            course.add_hole(hole_number, hole)
        return course


class HoleGenerator(object):
    @classmethod
    def generate(cls, hole_number):
        par = random.randint(3, 5)
        distance = random.randrange(250, 550, 50)
        return Hole(hole_number, par, distance)


class PlayersGenerator(object):
    @classmethod
    def _random_name(cls):
        return "Player " + str(int(random.random() * 1024))

    @classmethod
    def generate(cls, max_players=4):
        players = []
        for x in xrange(random.randint(1, max_players)):
            players.append(Player(cls._random_name()))
        return players

# vim: filetype=python
