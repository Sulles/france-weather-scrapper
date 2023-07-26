import argparse
import getopt
import sqlite3
import sys


def underscore_date(str_vals: str):
    return ArgDate(str_vals.split('_'))


parser = argparse.ArgumentParser(
    "main.py",
    "main.py -s dd_mm_yyyy -e dd_mm_yyyy -f m/d/h",
    description="Scrape historic weather data from https://www.infoclimat.fr/observations-meteo/archives")
parser.add_argument(
    "-s", "--start", required=True, dest="start", metavar="start_date", type=underscore_date,
    help="start date as dd_mm_yyyy")
parser.add_argument(
    "-e", "--end", required=True, dest="end", metavar="end_date", type=underscore_date,
    help="end date as dd_mm_yyyy")
parser.add_argument(
    "-f", "--freq", required=True, dest="freq", metavar="frequency", choices=["m", "d", "h"],
    help="frequency as either m, d, or h")


class ArgDate:
    Y: int
    M: int
    D: int

    def __init__(self, y_m_d: list) -> None:
        self.Y = y_m_d[0]
        self.M = y_m_d[1]
        self.D = y_m_d[2]


def main():
    pass


if __name__ == "__main__":

    print(parser.parse_args(sys.argv[1:]))

    main()
