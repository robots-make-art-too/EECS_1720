import argparse
import sys
from datetime import date
 
parser = argparse.ArgumentParser(description="Get day of the week from a date")
 
parser.add_argument("date", nargs="?", help="Date (mm/dd/yyyy)", default=None)
 
arguments = parser.parse_args()
 
use_arguments = True if arguments.date is not None else False
 
while True:
    if use_arguments:
        date_input = arguments.date
    else:
        date_input = input("Enter the date (mm/dd/yyyy): ")
 
    try:
        date_list = date_input.split("/")
        month = int(date_list[0])
        day = int(date_list[1])
        year = int(date_list[2])
 
        date_date = date(year, month, day)
    except:
        print("Invalid date")
        if use_arguments:
            sys.exit()
        continue
 
    break
 
n_day_of_week = date_date.weekday()
 
days_of_week = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)
 
day_of_week = days_of_week[n_day_of_week]
print(day_of_week)