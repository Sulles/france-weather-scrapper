from config import *
from util import *

if __name__ == "__main__":
    # grab all raw data
    csv_data = pd.read_csv(RAW_DATA_FILE_NAME, index_col=0)

    # convert data to list
    data_as_list = csv_data.values.tolist()

    # calculate mins, maxs, and hours colder/hotter than the mean
    hot_cold_stitches = calculate_stitches_new(data_as_list)

    # we want row names to be the dates
    row_names = csv_data.index.to_list()
    # we want column names to be the hot vs cold stitches
    column_names = ['Hot Stitches', 'Cold Stitches']
    print(write_csv_with_headings(hot_cold_stitches, row_names, column_names,
                                  STITCHING_GUIDE_FILE_NAME))
