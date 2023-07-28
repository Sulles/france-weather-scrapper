import argparse
import sqlite3
import sys

from util import *


# WARNING: the first day of the month is "1er", not "1", all other days are their int value
TARGET_SITE_ROOT = "https://www.infoclimat.fr/observations-meteo/archives"
TARGET_SITE_TAIL = "/albi-le-sequestre/07632.html"
TIME_DELTA = datetime.timedelta(1.0)


parser = argparse.ArgumentParser(
    "scrape.py",
    "scrape.py -s [dd_mm_yyyy] -e [dd_mm_yyyy] -f [m, d, or h]",
    description="Scrape historic weather data from https://www.infoclimat.fr/observations-meteo/archives")
parser.add_argument(
    "-s", "--start", required=True, dest="start", metavar="start_date", type=dd_mm_yyyy2date,
    help="start date as dd_mm_yyyy")
parser.add_argument(
    "-e", "--end", required=True, dest="end", metavar="end_date", type=dd_mm_yyyy2date,
    help="end date as dd_mm_yyyy")
parser.add_argument(
    "-f", "--freq", required=True, dest="freq", metavar="frequency", choices=['daily', 'hourly'], type=frequency_complete,
    help="frequency as either d or h (m not supported!)")


def main():
    args = parser.parse_args()
    assert args.start < args.end, "START DATE MUST OCCUR BEFORE END DATE"

    print(f"Launching scrapper on '{TARGET_SITE_ROOT}' for weather data from " +
          f"{args.start} to {args.end}")

    # set target_day to start
    target_day = args.start

    # while we're within bounds
    while target_day <= args.end:

        target_day += TIME_DELTA


if __name__ == "__main__":
    main()
