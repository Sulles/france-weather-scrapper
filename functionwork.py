# def calculate_stitches(temps_list: list[float]) -> tuple[int, int]:
#     ''' function to calculate hot and cold stitches given a list. Returns two ints '''

#     # Calculate average temperature
#     avg_temp = sum(temps_list) / len(temps_list)

#     # loop through temps to find how entries are hotter than average
#     hotter_than_avg_counter = 0
#     for temp in temps_list:
#         if temp >= avg_temp:
#             hotter_than_avg_counter += 1

#     # calc hot and cold stitches
#     hot_stitches = round(hotter_than_avg_counter / len(temps_list) * 250)
#     cold_stitches = 250 - hot_stitches

#     return hot_stitches, cold_stitches

import numpy as np

def calculate_stitches_new(temps_list: list[float]) -> tuple[int, int]:
    ''' function to calculate hot and cold stitches given a list. Returns two ints '''

    # Convert temps_list to numpy array
    temps_np = np.array(temps_list)

    # Calculate average temperature using numpy
    avg_temp = temps_np.mean()

    # Calculate boolean mask of temperatures hotter than average
    hotter_than_avg_mask = temps_np >= avg_temp

    # Count the number of temperatures hotter than average
    hotter_than_avg_counter = np.sum(hotter_than_avg_mask)

    # Calculate hot and cold stitches
    hot_stitches = round(hotter_than_avg_counter / len(temps_list) * 250)
    cold_stitches = 250 - hot_stitches

    return hot_stitches, cold_stitches

# Given list of temperatures
temps_list = [10.8, 10.8, 11.9, 13.5, 13.9, 15, 17, 15.9, 19.1, 17.8,
                14.4, 18.5, 15.8, 15.3, 14.4, 12.2, 12.1, 12.8, 12.6,
                12.4, 11.9, 11.5, 11.9, 12]

# Calculate hot and cold stitches
hot_stitches, cold_stitches = calculate_stitches_new(temps_list)

# Print output
print('Hot stitches:', hot_stitches)
print('Cold stitches:', cold_stitches)


from util import calculate_stitches
if __name__ == '__main__':
    import timeit
    time_method_one = timeit.timeit("calculate_stitches(temps_list)", globals=globals(), number = 100000)
    time_method_two = timeit.timeit("calculate_stitches_new(temps_list)", globals=globals(), number = 100000)

    print(f"Method One: {time_method_one:.6f} seconds")
    print(f"Method Two: {time_method_two:.6f} seconds")

