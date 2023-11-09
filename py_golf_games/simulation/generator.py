#!/usr/bin/env python

import random
import typing

from ..course import Course
from ..hole import Hole
from ..player import Gender
from ..player import Player
from ..round import Round
from ..tee import Tee
from ..tee import TeeMarker


class CourseGenerator:
    @classmethod
    def generate(cls, name: str, num_holes: int) -> Course:
        course = Course(name)
        for hole_number in range(1, num_holes + 1):
            hole = HoleGenerator.generate(hole_number)
            course.add_hole(hole_number, hole)
        return course


class HoleGenerator:
    @classmethod
    def generate(cls, hole_number: int) -> Hole:
        tees = TeesGenerator.generate()
        return Hole(hole_number, tees)


class TeesGenerator:
    @classmethod
    def generate(cls) -> typing.Dict[TeeMarker, Tee]:
        tees = {}
        for marker in list(TeeMarker):
            tee = TeeGenerator.generate(marker)
            tees[marker] = tee
        return tees


class TeeGenerator:
    @classmethod
    def generate(cls, tee_marker: TeeMarker) -> Tee:
        par = random.randint(3, 5)
        distance = random.randrange(250, 550, 50)
        return Tee(tee_marker, par, distance)


class PlayersGenerator:
    @classmethod
    def _random_name(cls) -> str:
        return "Player " + str(int(random.random() * 1024))

    @classmethod
    def _random_gender(cls) -> Gender:
        return random.choice(list(Gender))

    @classmethod
    def generate(cls, max_players: int = 4) -> typing.List[Player]:
        players = []
        for _ in range(random.randint(1, max_players)):
            players.append(Player(cls._random_name(), cls._random_gender()))
        return players


class RoundGenerator:
    @classmethod
    def generate(cls, course: Course, players: typing.List[Player]) -> Round:
        golf_round = Round(course, players)

        for player in players:
            for hole in range(1, len(course.holes) + 1):
                strokes = random.randint(3, 10)
                golf_round.record_score(player, hole, strokes)

        return golf_round


# vim: filetype=python
