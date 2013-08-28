#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import traceback
import sys

from player import Player
from course import Course
from hole import Hole
from round import Round

import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

def create_hole(hole_number):
    par = random.randint(3, 5)
    distance = random.randrange(250, 550, 50)
    return Hole(hole_number, par, distance)

if __name__ == '__main__':
    try:
        players = []

        for x in xrange(random.randint(1, 4)):
            rand = int(random.random() * 1024)
            players.append(Player("Player " + str(rand)))

        course = Course("Ala Wai")

        for hole_number in xrange(1, 19):
            hole = create_hole(hole_number)
            course.add_hole(hole_number, hole)

        logging.debug(course)

        for hole in course.holes:
            logging.debug(hole)

        print ""

        round = Round(course, players)

        for player in players:
            for hole in xrange(1, 19):
                strokes = random.randint(3, 10)
                round.record_score(player, hole, strokes)

        for player in players:
            logging.debug(player)

            scores = round.scorecard.get_scores(player)

            total = 0

            for hole_score in scores:
                logging.debug("Hole {0} - Score {1}".format(hole_score.hole_number,
                    hole_score.score))
                total += hole_score.score

            logging.debug("Total {0}".format(total))

    except:
        trace = traceback.format_exc()
        logging.error("OMGWTFBBQ: {0}".format(trace))
        sys.exit(1)

    sys.exit(0)

# vim: filetype=python
