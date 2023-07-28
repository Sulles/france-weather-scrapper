import datetime
import subprocess


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
    return frequency_dict[first_letter]


def calculate_stitches(temps_list: list[float]) -> tuple[int, int]:
    ''' function to calculate hot and cold stitches given a list. Returns two ints '''

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


print(__name__)

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
