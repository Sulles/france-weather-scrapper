#take list of temps from suley
temps_list = [10.8,
10.8,
11.9,
13.5,
13.9,
15,
17,
15.9,
19.1,
17.8,
14.4,
18.5,
15.8,
15.3,
14.4,
12.2,
12.1,
12.8,
12.6,
12.4,
11.9,
11.5,
11.9,
12]

#get average temp
avg_temp = sum(temps_list) / len(temps_list)

#loop through temps to find how entries are hotter than average
hotter_than_avg_counter = 0
for temp in temps_list:
    if temp >= avg_temp:
        hotter_than_avg_counter += 1

#calc percent hotter than average
percent_hotter_than_avg = hotter_than_avg_counter / len(temps_list) * 100
print(percent_hotter_than_avg)