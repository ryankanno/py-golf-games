#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hole import Hole


class Course(object):
    def __init__(self, name, *args, **kwargs):
        super(Course, self).__init__(*args, **kwargs)
        self._name = name
        self._holes = {}

    def add_hole(self, hole_number, hole):
        self._holes[hole_number] = hole

    def get_hole(self, hole_number):
        return self._holes[hole_number] if hole_number in self._holes else None

    @property
    def holes(self):
        return self._holes.values()

    @property
    def name(self):
        return self._name

    @property
    def total_distance(self):
        return sum([hole.distance for hole in self.holes])

    @property
    def total_par(self):
        return sum([hole.par for hole in self.holes])

    def __str__(self):
        return self.name

# vim: filetype=python
