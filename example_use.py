from util import calculate_stitches_new, write_csv_with_headings
import pandas as pd
import numpy as np

# Example building of list of lists of temperatures to be replaced
temps_list_1 = [10.8, 10.8, 11.9, 13.5, 13.9, 15, 17, 15.9, 19.1, 17.8,
                14.4, 18.5, 15.8, 15.3, 14.4, 12.2, 12.1, 12.8, 12.6,
                12.4, 11.9, 11.5, 11.9, 12]
temps_list_2 = [13.8, 13, 13.1, 15.2, 17.9, 21.5, 21.8, 21.8, 21.5,
                21, 20.3, 19.3, 18, 17.4, 15.4, 12.9, 10.8, 8.4, 7.6,
                7.7, 8.1, 8.2, 9, 10.2]

df = pd.read_csv('raw_data.csv')

# Step 2: Set the 'Date' column as the index (if it's not already the index)
# This step is necessary to use the .loc attribute with the date index.
df.set_index('Date', inplace=True)

# Step 3: Pull data from the row with the specified index '26 juillet 2023'
row_26_juillet_2023 = df.loc['26 juillet 2023']

# Step 4: Display the data from the row
print(row_26_juillet_2023)

# Get list_of_lists_from_suleyman from suleyman
list_of_lists_from_suleyman = [temps_list_1, temps_list_2]

from config import *
from util import *

# grab all raw data
csv_data = pd.read_csv(RAW_DATA_FILE_NAME, index_col=0)

# calculate mins, maxs, and hours colder/hotter than the mean
# def calculate_stitches(temps_list: list[float]) -> tuple[int, int]:
data_as_list = csv_data.values.tolist()
hot_cold_stitches = calculate_stitches_new(data_as_list)
print(write_csv_with_headings(hot_cold_stitches, csv_data.index.to_list(),
                              STITCHING_GUIDE_FILE_NAME))
