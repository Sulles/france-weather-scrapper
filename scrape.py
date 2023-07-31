import argparse
from bs4 import BeautifulSoup
import sqlite3
import re
import requests
import time

from util import *


# WARNING: the first day of the month is "1er", not "1", all other days are their int value
TARGET_SITE_ROOT = "https://www.infoclimat.fr/observations-meteo/archives"
TARGET_SITE_TAIL = "albi-le-sequestre/07632.html"
TIME_DELTA = datetime.timedelta(1.0)
CSV_FILE_NAME = "raw_data.csv"


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
    help="frequency as h (neither d nor m are supported!)")


def add_data_to_csv(date_str: str, temps: list[float]):
    # load existing csv
    csv_data = pd.read_csv(CSV_FILE_NAME, index_col=0)

    # fill temps with NaN if not 24 elements long
    temps.extend([np.NAN for _ in range(0, 24 - len(temps))])

    # edit existing row if date already exists, otherwise create a new one
    if date_str in csv_data.index:
        print(f"WARNING: Overwriting existing date for '{date_str}'!")
    else:
        print(f"Creating new entry for '{date_str}!")
    csv_data.loc[date_str] = temps

    # save csv data
    csv_data.to_csv(CSV_FILE_NAME)


def main():
    args = parser.parse_args()
    assert args.start < args.end, "START DATE MUST OCCUR BEFORE END DATE"

    print(f"Launching scrapper on '{TARGET_SITE_ROOT}' for weather data from " +
          f"{args.start} to {args.end}")

    # # define list of dates to save
    # all_dates: list[str] = []

    # # define list of list of temperatures to save
    # all_temps: list[list[float]] = []

    # define reg expression to get temp from html poopoo
    temp_expr = ">\D*(\d*.\d*)\D*</span>"

    # set target_day to start
    target_day: datetime.date = args.start

    # while we're within bounds
    while target_day <= args.end:

        # define target website

        # get day string
        day_str = str(target_day.day)
        if day_str == "1":
            day_str = "1er"

        # get month string
        month_str = monthNum2str_fr[target_day.month]

        # get year string
        year_str = str(target_day.year)

        # make date string
        date_str = f"{day_str}/{month_str}/{year_str}"

        # create target url
        target_url = TARGET_SITE_ROOT + "/" + date_str + "/" + TARGET_SITE_TAIL
        print(target_url)

        # get website data from target url
        target_page = requests.get(target_url)

        # parse target page content for temperatures
        soup = BeautifulSoup(target_page.content, "html.parser")
        match_temp_lines = soup.find_all("span", class_="tipsy-trigger",
                                         style="font-weight:bold;display:inline-block;font-size:16px")
        regex_matches = re.findall(temp_expr, str(match_temp_lines))

        # save target date and temps to all data
        add_data_to_csv(date_str.replace("/", " "),
                        [float(_) for _ in regex_matches])
        # all_dates.append(date_str.replace("/", " "))
        # all_temps.append(regex_matches)

        # # save to file
        # with open(f"{date_str}.txt", 'w') as file:
        #     soup = BeautifulSoup(target_page.content, "html.parser")
        #     file.write(soup.prettify())
        #     temps = soup.find_all("span", class_="tipsy-trigger",
        #                           style="font-weight:bold;display:inline-block;font-size:16px")
        #     with open(f"{day_str}_{month_str}_{year_str}_only_temps_hopefully.txt", 'w') as temps_file:
        #         temps_file.writelines(
        #             [str(garbage_string)[-11:-7] + "\n" for garbage_string in temps])

        # increment target day and sleep to not accidentally go on the DDOS list
        time.sleep(5.0)
        target_day += TIME_DELTA

    # # create data frame with all data
    # csv_data = pd.DataFrame(all_temps, index=all_dates)
    # csv_data.to_csv(CSV_FILE_NAME)


if __name__ == "__main__":
    main()
