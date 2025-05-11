from pathlib import Path
import csv
from datetime import datetime

path = Path('D:\python\data_visualization_with_python\weather_data\sitka_weather_07-2021_simple.csv')

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