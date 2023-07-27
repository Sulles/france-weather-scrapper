import datetime


def date_from_day_month_year(str_vals: str):
    day_month_year: list(int) = [int(_) for _ in str_vals.split('_')]
    year_month_day = day_month_year[::-1]
    return datetime.date(year_month_day[0], year_month_day[1], year_month_day[2])


def frequency_complete(first_letter: str):
    frequency_dict = dict(m="monthly", d="daily", h="hourly")
    return frequency_dict[first_letter]
