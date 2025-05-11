from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('D:\python\data_visualization_with_python\weather_data\sitka_weather_2021_simple.csv')

#Print the header row
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
print("\nHeader Row:")
print(header_row)

#Print the first row
first_row = next(reader)
print("\nFirst Row:")
print(first_row, '\n')

#Print headers with their positions
for index, header in enumerate(header_row):
    print(f"{index}  {header}")

dates = []

#Reinitialize the reader
reader = csv.reader(lines)
#Skips the header row
next(reader)

#Convert datestring into a date object
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(date)

tmax = []

#Reinitialize the reader
reader = csv.reader(lines)
#Skips the header row
next(reader)

#Convert string into a int
for row in reader:
    max = int(row[4])
    tmax.append(max)

print("\nMaximim Temperatures:")
print(tmax)

tmin = []

#Reinitialize the reader
reader = csv.reader(lines)
#Skips the header row
next(reader)

#Convert string into a int
for row in reader:
    min = int(row[5])
    tmin.append(min)

print("\nMinimum Temperatures:")
print(tmin)

year_month = [date.strftime("%Y-%m") for date in dates]

#Plot for high temperaturs
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(10, 7))
ax.plot(dates, tmax, color='red')

ax.set_title("Daily High Temperature, July-2021", fontsize=25)
ax.set_xlabel('Day', fontsize=15)
ax.set_ylabel('Temperature', fontsize=15)
fig.autofmt_xdate()
ax.tick_params(labelsize=16)

plt.savefig('output1.png', bbox_inches = 'tight')

#Plot for high temperaturs
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(10, 7))
ax.plot(dates, tmin, color='blue')

ax.set_title("Daily Low Temperature, July-2021", fontsize=25)
ax.set_xlabel('Day', fontsize=15)
ax.set_ylabel('Temperature', fontsize=15)
fig.autofmt_xdate()
ax.tick_params(labelsize=16)

plt.savefig('output2.png', bbox_inches = 'tight')

#Plotting both
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(10, 7))
ax.plot(dates, tmax, color='red')
ax.plot(dates, tmin, color='blue')
ax.fill_between(dates, tmax, tmin, facecolor = 'blue', alpha = 0.1)

ax.set_title("Daily High and Low Temperature, July-2021", fontsize=25)
ax.set_xlabel('Day', fontsize=15)
ax.set_ylabel('Temperature', fontsize=15)
fig.autofmt_xdate()
ax.tick_params(labelsize=16)

plt.savefig('output3.png', bbox_inches = 'tight')