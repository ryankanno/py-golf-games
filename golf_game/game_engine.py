#!/usr/bin/env python
# -*- coding: utf-8 -*-


class GameEngine(object):
    def __init__(self, *args, **kwargs):
        super(GameEngine, self).__init__(*args, **kwargs)
        self._games = []

    def enable_game(self, game):
        self._games.append(game)
