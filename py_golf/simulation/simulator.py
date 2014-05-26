#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import traceback
import sys

from generator import CourseGenerator
from generator import HoleGenerator
from generator import PlayersGenerator
from generator import RoundGenerator
from tee import TeeMarker

import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def spaces(curr, max):
    spaces_to_print = ""
    for x in xrange(max - curr):
        spaces_to_print += " "
    return spaces_to_print


def print_header(header, max_len):
    print header + spaces(len(header), max_len),

def pretty_print(round):
    print "--------------------"
    print round.course
    print "--------------------"

    max_len = 0
    for player in round.players:
        curr = len(player.name)
        max_len = curr if curr > max_len else max_len

    print_header("Hole", max_len)
    for hole in round.course.holes:
        if (hole.number == 1): print " ",
        print str(hole.number) + "  | ",

    print ""

    for marker in list(TeeMarker):
        print_header(marker.name, max_len)
        for hole in round.course.holes:
            tee = hole.get_tee(marker)
            if (hole.number == 1): print "",
            if (hole.number > 9):
                print str(tee.distance) + "  |",
            else:
                print str(tee.distance) + " |",
        print round.course.total_distance(marker)

        print_header("", max_len)
        for hole in round.course.holes:
            tee = hole.get_tee(marker)
            if (hole.number == 1): print "",
            if (hole.number > 9):
                print str(tee.par) + "  |",
            else:
                print str(tee.par) + " |",
        print ""

    for player in round.players:
        print_header(player.name, max_len)
        for hole in round.course.holes:
            if (hole.number == 1): print "",
            if (hole.number > 9):
                print str(round.scorecard.get_score(player, hole.number).score) + "  |",
            else:
                print str(round.scorecard.get_score(player, hole.number).score) + "  |",

        print round.scorecard.get_scores(player).total_score,
        print ""


if __name__ == '__main__':
    try:
        players = PlayersGenerator.generate();
        course = CourseGenerator.generate("Makalena", 18)
        round = RoundGenerator.generate(course, players)

        for player in players:
            logging.debug(player)

            scores = round.scorecard.get_scores(player)

            total = 0

            for hole_score in scores:
                logging.debug("Hole {0} - Score {1}".format(hole_score.hole_number,
                    hole_score.score))
                total += hole_score.score

            logging.debug("Total {0}".format(total))

        pretty_print(round)

    except:
        trace = traceback.format_exc()
        logging.error("OMGWTFBBQ: {0}".format(trace))
        sys.exit(1)

    sys.exit(0)

# vim: filetype=python
