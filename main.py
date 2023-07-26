import argparse
import getopt
import sqlite3
import sys


def underscore_date(str_vals: str):
    y, m, d = str_vals.split('_')


parser = argparse.ArgumentParser(
    "main.py",
    "main.py -s dd_mm_yyyy -e dd_mm_yyyy -f m/d/h",
    description="Scrape historic weather data from https://www.infoclimat.fr/observations-meteo/archives")
parser.add_argument(
    "-s", "--start", required=True, dest="start", metavar="start_date",
    help="start date as dd_mm_yyyy")
parser.add_argument(
    "-e", "--end", required=True, dest="end", metavar="end_date",
    help="end date as dd_mm_yyyy")
parser.add_argument(
    "-f", "--freq", required=True, dest="freq", metavar="frequency", choices=["m", "d", "h"],
    help="frequency as either m, d, or h")
parser.print_help()


class ArgDate:
    Y: int
    M: int
    D: int

    def __init__(self, y, m, d) -> None:
        self.Y = y
        self.M = m
        self.D = d


def main():
    # Arguments:
    # start_date = dd-mm-yyyy
    # end_date = dd-mm-yyyy
    # frequency = monthly/daily/hourly
    print(str(sys.argv))

    pass


if __name__ == "__main__":

    def print_usage():
        print("Failed to parse arguments, usage: main.py -s <start_date> -e <end_date> -f <frequency>")

    try:
        opts, args = getopt.getopt(
            sys.argv[1:], "s:e:f:", ["start_date", "end_date", "frequency"])
    except getopt.GetoptError:
        print_usage()

    for opt, arg in opts:
        print(f"parsing {opt} = {arg}")

    main()
