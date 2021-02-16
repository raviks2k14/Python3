import csv
import matplotlib.pyplot as plt
from datetime import datetime

# filename = "../data/sitka_weather_07-2018_simple.csv"
filename = "../data/sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

    # Get high temperatures from this file
    dates, precips = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        precip = float(row[3])
        precips.append(precip)

    # print(highs)

# Plot the high temperature
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precips, c='blue')

# Format plot.
ax.set_title("Daily Rainfall Amounts - 2018", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall (in)", fontsize=16)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

