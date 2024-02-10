from config import *
from util import *

if __name__ == "__main__":
    # grab all raw data
    csv_data = pd.read_csv(RAW_DATA_FILE_NAME, index_col=0)

    # calculate mins, maxs, and hours colder/hotter than the mean
    # def calculate_stitches(temps_list: list[float]) -> tuple[int, int]:
    data_as_list = csv_data.values.tolist()
    hot_cold_stitches = calculate_stitches_new(data_as_list)
    print(write_csv_with_headings(hot_cold_stitches, csv_data.index.to_list(),
                                  STITCHING_GUIDE_FILE_NAME))
