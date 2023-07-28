import numpy as np
import pandas as pd

def calculate_stitches_new(temps_list: list[list[float]]) -> list[tuple[int, int]]:
    ''' function to calculate hot and cold stitches given a list of lists. Returns a list of tuples '''

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

# Example building of list of lists of temperatures to be replaced
temps_list_1 = [10.8, 10.8, 11.9, 13.5, 13.9, 15, 17, 15.9, 19.1, 17.8,
                14.4, 18.5, 15.8, 15.3, 14.4, 12.2, 12.1, 12.8, 12.6,
                12.4, 11.9, 11.5, 11.9, 12]
temps_list_2 = [13.8, 13, 13.1, 15.2, 17.9, 21.5, 21.8, 21.8, 21.5, 
                21, 20.3, 19.3, 18, 17.4, 15.4, 12.9, 10.8, 8.4, 7.6, 
                7.7, 8.1, 8.2, 9, 10.2]
#Get list_of_lists_from_suleyman from suleyman
list_of_lists_from_suleyman = [temps_list_1, temps_list_2]

data = calculate_stitches_new(list_of_lists_from_suleyman)
print(data)

#headings and csv stuff
row_names = ['May 1st', 'May 2nd']
column_names = ['Hot Stitches', 'Cold Stitches']
dataframe = pd.DataFrame(data, index= row_names, columns= column_names)
dataframe.to_csv('stitching_guide.csv')
print(dataframe)