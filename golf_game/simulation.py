#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import traceback
import sys

from player import Player
from course import Course
from hole import Hole
from round import Round

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

if __name__ == '__main__':
    try:
        player1, player2, player3, player4 = Player("1"), Player("2"), Player("3"), Player("4")
        players = [player1, player2, player3, player4]

        course = Course("Ala Wai")
        hole1 = Hole(1, 4, 425)
        hole2 = Hole(2, 5, 540)
        hole6 = Hole(6, 3, 200)
        course.add_hole(1, hole1)
        course.add_hole(6, hole6)
        course.add_hole(2, hole2)

        logging.debug(course)

        for hole in course.holes:
            logging.debug(hole)

        round = Round(course, players)
        round.record_score(player1, 2, 3)
        round.record_score(player2, 2, 2)
        round.record_score(player2, 1, 3)

        p1_scores = round.scorecard.get_scores(player1)
        p2_scores = round.scorecard.get_scores(player2)

        for score in p1_scores:
            print score

    except:
        trace = traceback.format_exc()
        logging.error("OMGWTFBBQ: {0}".format(trace))
        sys.exit(1)

    sys.exit(0)

# vim: filetype=python
