import datetime
import subprocess
import numpy as np
import pandas as pd


def dd_mm_yyyy2date(dd_mm_yyyy: str):
    ''' convert dd_mm_yyyy string to datetime.date '''
    # separate day, month, and year
    dd_mm_yyyy: list(int) = [int(_) for _ in dd_mm_yyyy.split('_')]
    # invert to datetime.date format of year, month, day
    yyyy_mm_dd = dd_mm_yyyy[::-1]
    # return datetime.date object
    return datetime.date(yyyy_mm_dd[0], yyyy_mm_dd[1], yyyy_mm_dd[2])


def frequency_complete(first_letter: str):
    ''' verbose frequency, convert... m -> monthly, d -> daily, h -> hourly '''
    frequency_dict = dict(m="monthly", d="daily", h="hourly")
    # if people provided the whole word instead of the first letter
    if first_letter in frequency_dict.values():
        return first_letter
    return frequency_dict[first_letter]


def calculate_stitches(temps_list: list[float]) -> tuple[int, int]:
    ''' loop through temps list to calculate hot and cold stitches given a list. Returns two ints '''

    # Calculate average temperature
    avg_temp = sum(temps_list) / len(temps_list)

    # loop through temps to find how entries are hotter than average
    hotter_than_avg_counter = 0
    for temp in temps_list:
        if temp >= avg_temp:
            hotter_than_avg_counter += 1

    # calc hot and cold stitches
    hot_stitches = round(hotter_than_avg_counter / len(temps_list) * 250)
    cold_stitches = 250 - hot_stitches

    return hot_stitches, cold_stitches

def calculate_stitches_new(temps_list: list[list[float]]) -> list[tuple[int, int]]:
    ''' list comparison to calculate hot and cold stitches given a list of lists. Returns a list of tuples '''

    # Convert temps to numpy array
    temps_np = np.array(temps_list)

    # Calculate average temperature using numpy
    avg_temp = np.mean(temps_np, axis=1).reshape((len(temps_list), 1))

    # Calculate boolean mask of temperatures hotter than average
    hotter_than_avg_mask = temps_np >= avg_temp

    # Count the number of temperatures hotter than average
    hotter_than_avg_counter = np.sum(hotter_than_avg_mask, axis=1)

    # Calculate hot and cold stitches
    hot_stitches = np.rint(hotter_than_avg_counter / len(temps_list[0]) * 250)
    cold_stitches = 250 - hot_stitches
    stitches = np.vstack((hot_stitches, cold_stitches)).astype(int).T

    return stitches

def write_csv_with_headings(stitches_calced: list[tuple[int, int]]) -> pd:
    ''' create csv with row and column names, returns dataframe '''

    #headings and csv stuff
    row_names = ['May 1st', 'May 2nd']
    column_names = ['Hot Stitches', 'Cold Stitches']
    dataframe = pd.DataFrame(data, index= row_names, columns= column_names)
    dataframe.to_csv('stitching_guide.csv')
    return dataframe

if __name__ == "__main__":

    # Given list of temperatures
    temps_list = [10.8, 10.8, 11.9, 13.5, 13.9, 15, 17, 15.9, 19.1, 17.8,
                  14.4, 18.5, 15.8, 15.3, 14.4, 12.2, 12.1, 12.8, 12.6,
                  12.4, 11.9, 11.5, 11.9, 12]

    # Calculate hot and cold stitches
    hot_stitches, cold_stitches = calculate_stitches(temps_list)

    # Print output
    print('Hot stitches:', hot_stitches)
    print('Cold stitches:', cold_stitches)
