import datetime
import subprocess
import numpy as np
import pandas as pd

from config import STITCHES_PER_DAY, STITCHING_GUIDE_FILE_NAME
from pathlib import Path

# convert month number to french month string
monthNum2str_fr = [IndexError, 'janvier', 'fevrier', 'mars', 'avril', 'mai',
                   'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'decembre']


def dd_mm_yyyy2date(dd_mm_yyyy: str):
    """ convert dd_mm_yyyy string to datetime.date """
    # separate day, month, and year
    dd_mm_yyyy: list(int) = [int(_) for _ in dd_mm_yyyy.split('_')]
    # invert to datetime.date format of year, month, day
    yyyy_mm_dd = dd_mm_yyyy[::-1]
    # return datetime.date object
    return datetime.date(yyyy_mm_dd[0], yyyy_mm_dd[1], yyyy_mm_dd[2])


def frequency_complete(first_letter: str):
    """ verbose frequency, convert... m -> monthly, d -> daily, h -> hourly """
    frequency_dict = dict(m="monthly", d="daily", h="hourly")
    # if people provided the whole word instead of the first letter
    if first_letter in frequency_dict.values():
        return first_letter
    return frequency_dict[first_letter]


def calculate_stitches(temps_list: list[float]) -> tuple[int, int]:
    """ loop through temps list to calculate hot and cold stitches given a list. Returns two ints """

    # Calculate average temperature
    avg_temp = sum(temps_list) / len(temps_list)

    # loop through temps to find how entries are hotter than average
    hotter_than_avg_counter = 0
    for temp in temps_list:
        if temp >= avg_temp:
            hotter_than_avg_counter += 1

    # calc hot and cold stitches
    hot_stitches = round(hotter_than_avg_counter /
                         len(temps_list) * STITCHES_PER_DAY)
    cold_stitches = STITCHES_PER_DAY - hot_stitches

    return hot_stitches, cold_stitches


def calculate_stitches_new(temps_list: list[list[float]]) -> list[tuple[int, int]]:
    """ list comparison to calculate hot and cold stitches given a list of lists. Returns [(hot, cold)] """

    # Convert temps to numpy array
    temps_np = np.array(temps_list)

    # Calculate average temperature using numpy
    avg_temp = np.nanmean(temps_np, axis=1).reshape((len(temps_list), 1))

    # Calculate boolean mask of temperatures hotter than average
    hotter_than_avg_mask = temps_np >= avg_temp

    # Count the number of temperatures hotter than average
    hotter_than_avg_counter = np.sum(hotter_than_avg_mask, axis=1)

    # Calculate hot and cold stitches
    hot_stitches = np.rint(hotter_than_avg_counter /
                           len(temps_list[0]) * STITCHES_PER_DAY)
    cold_stitches = STITCHES_PER_DAY - hot_stitches
    stitches = np.vstack((hot_stitches, cold_stitches)).astype(int).T

    return stitches


def write_csv_with_headings(
        stitches_calced: list[tuple[int, int]], row_names: list[str], column_names: list[str],
        csv_file_name: Path) -> pd:
    """ create csv with row and column names, returns dataframe """

    # headings and csv stuff
    dataframe = pd.DataFrame(
        stitches_calced, index=row_names, columns=column_names)
    dataframe.to_csv(csv_file_name)

    return dataframe


# Timer to compare functions
if __name__ == "__main__":
    import timeit

    time_method_one = timeit.timeit(
        "calculate_stitches(temps_list)", globals=globals(), number=100000)
    time_method_two = timeit.timeit(
        "calculate_stitches_new(temps_list)", globals=globals(), number=100000)

    print(f"Method One: {time_method_one:.6f} seconds")
    print(f"Method Two: {time_method_two:.6f} seconds")
