#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Player(object):
    def __init__(self, name, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        self._name = name

    def __str__(self):
        return self._name

# vim: filetype=python
