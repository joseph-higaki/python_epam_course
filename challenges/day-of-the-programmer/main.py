#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
# 20:06
# 21:04

def dayOfProgrammer(year):
    # Write your code here
    def julian_leap(year):
        return  (year  % 4 == 0)
    def gregorian_leap(year):
        return (year % 400 == 0) or ((year  % 4 == 0) and (year % 100 != 0))
        
    def calculate_february_days(year):
        if (1700 <= year and year <= 1917): 
            return 29 if julian_leap(year) else 28
        elif (year == 1918):
            return (29 if gregorian_leap(year) else 28) - 13
        elif (1919 <= year and year <= 2700): 
            return 29 if gregorian_leap(year) else 28 
        
    def calendar_days_array(year):
        return_value = {
           1: 31, 
           2: calculate_february_days(year),
           3: 31,
           4: 30,
           5: 31,
           6: 30,
           7: 31,
           8: 31,
           9: 30,
           10: 31,
           11: 30,
           12: 31
        }    
        return return_value
        
    def find_month_day(days_array, day_of_year):
        total_days = 0
        for month, days_in_month in days_array.items():
            if day_of_year < total_days + days_in_month:
                return month, day_of_year - total_days
            else:
                total_days += days_in_month
            
    #print(calendar_days_array(1917))
    #print(calendar_days_array(1918))
    #print(calendar_days_array(1919))
    #print(find_month_day(calendar_days_array(1918), 32))
    #print(find_month_day(calendar_days_array(1918), 256))
    #print(find_month_day(calendar_days_array(1919), 32))
    #print(find_month_day(calendar_days_array(1919), 62))
    #print(find_month_day(calendar_days_array(1919), 256))
    #print(find_month_day(calendar_days_array(1984), 256))
    month_day = find_month_day(calendar_days_array(year), 256)
    result = f"{month_day[1]}.{month_day[0]:02}.{year}"
    print(result)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
