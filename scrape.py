import argparse
import sqlite3
import sys

from util import date_from_day_month_year, frequency_complete


parser = argparse.ArgumentParser(
    "scrape.py",
    "scrape.py -s dd_mm_yyyy -e dd_mm_yyyy -f m/d/h",
    description="Scrape historic weather data from https://www.infoclimat.fr/observations-meteo/archives")
parser.add_argument(
    "-s", "--start", required=True, dest="start", metavar="start_date", type=date_from_day_month_year,
    help="start date as dd_mm_yyyy")
parser.add_argument(
    "-e", "--end", required=True, dest="end", metavar="end_date", type=date_from_day_month_year,
    help="end date as dd_mm_yyyy")
parser.add_argument(
    "-f", "--freq", required=True, dest="freq", metavar="frequency", type=frequency_complete,
    help="frequency as either m, d, or h")


def main():
    args = parser.parse_args()
    print(args)
    print(type(args))


if __name__ == "__main__":
    main()
