#!/usr/bin/env python

import logging
import sys
import traceback

from ..round import Round
from ..tee import TeeMarker
from .generator import CourseGenerator
from .generator import PlayersGenerator
from .generator import RoundGenerator


logging.basicConfig(
    level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s'
)


COLUMN_WIDTH = 5

NUM_HALF_HOLES = 9


def print_header(header: str, max_len: int) -> None:
    print(
        header.ljust(max_len),
    )


def print_column(value: int, hole_number: int) -> None:
    width = COLUMN_WIDTH + 1 if hole_number > NUM_HALF_HOLES else COLUMN_WIDTH
    sys.stdout.write(str(value).center(width, " ") + "|")


def print_separator_header(max_player_name_length: int) -> None:
    scorecard_length = max_player_name_length + 18 + (9 * 5) + (9 * 6) + 6
    print("-" * scorecard_length)


def pretty_print(golf_round: Round) -> None:
    print("--------------------")
    print(golf_round.course)
    print("--------------------")

    max_len = 0

    for player in golf_round.players:
        curr = len(player.name)
        max_len = max(max_len, curr)

    print_header("Hole", max_len)
    for hole in golf_round.course.holes:
        print_column(hole.number, hole.number)
    print()

    print_separator_header(max_len)

    for marker in list(TeeMarker):
        print_header(marker.name, max_len)
        for hole in golf_round.course.holes:
            tee = hole.get_tee(marker)
            if tee:
                print_column(tee.distance, hole.number)
        print(" " + str(golf_round.course.total_distance(marker)))

        print_header("", max_len)
        for hole in golf_round.course.holes:
            tee = hole.get_tee(marker)
            if tee:
                print_column(tee.par, hole.number)
        print()

    print_separator_header(max_len)

    for player in golf_round.players:
        print_header(player.name, max_len)
        for hole in golf_round.course.holes:
            hole_score = golf_round.scorecard.get_score(player, hole.number)
            if hole_score:
                print_column(hole_score.score, hole.number)
        player_score = golf_round.scorecard.get_scores(player)
        if player_score:
            print(" " + str(player_score.total_score))


if __name__ == '__main__':
    try:
        players = PlayersGenerator.generate()
        course = CourseGenerator.generate("Makalena", 18)
        golf_round = RoundGenerator.generate(course, players)

        pretty_print(golf_round)
    except:  # noqa: E722,B001
        trace = traceback.format_exc()
        logging.exception("OMGWTFBBQ: %s", trace)

        sys.exit(1)

    sys.exit(0)

# vim: filetype=python
