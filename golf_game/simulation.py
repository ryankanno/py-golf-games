#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import traceback
import sys

from round import Round

from simulation_generator import CourseGenerator
from simulation_generator import HoleGenerator
from simulation_generator import PlayersGenerator

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

    print_header("Par", max_len)
    for hole in round.course.holes:
        if (hole.number == 1): print " ",
        if (hole.number > 9): 
            print str(hole.par) + "   | ",
        else:
            print str(hole.par) + "  | ",

    print ""

    print_header("Distance", max_len)
    for hole in round.course.holes:
        if (hole.number == 1): print "",
        if (hole.number > 9): 
            print str(hole.distance) + "  |",
        else:
            print str(hole.distance) + " |",

    print ""

    for player in round.players:
        print_header(player.name, max_len)
        for hole in round.course.holes:
            if (hole.number == 1): print "",
            if (hole.number > 9): 
                print str(round.scorecard.get_score(player, hole.number).score) + "  |",
            else:
                print str(round.scorecard.get_score(player, hole.number).score) + "  |",
        print ""


if __name__ == '__main__':
    try:
        players = PlayersGenerator.generate();
        course = CourseGenerator.generate("Makalena", 18)
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

        pretty_print(round)

    except:
        trace = traceback.format_exc()
        logging.error("OMGWTFBBQ: {0}".format(trace))
        sys.exit(1)

    sys.exit(0)

# vim: filetype=python
