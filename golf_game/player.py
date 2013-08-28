#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Player(object):
    def __init__(self, name, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        self.name = name

# vim: filetype=python
