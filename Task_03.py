from datetime import datetime, date, timedelta
import calendar

# ------------------------------------------

"""
1.  Write a Python script to display the various Date Time formats
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week
"""

# today = date.today()
# print('Current date and time: ', datetime.now())
# print('Current year', today.year)
# print('Month of year', today.strftime("%m"))
# print('Week number of the year', today.strftime("%V"))
# print('Weekday of the week', today.weekday())
# print('Day of year', datetime.now().timetuple().tm_yday)
# print('Day of the month', today.strftime("%d"))
# print('Day of week', today.strftime("%A"))
# print(datetime.month(2022))
# ------------------------------------------

"""
2. Write a Python program to determine whether a given year is a leap year.
"""
# user_input = int(input("Enter the year: "))
# if calendar.isleap(user_input):
#     print("This is Leap year: ", user_input)
# else:
#     print("This is Not Leap year: ", user_input)

# ------------------------------------------


"""
3. Write a Python program to convert a string to datetime.
Sample String : Jan 1 2014 2:43PM
Expected Output : 2014-07-01 14:43:00
"""

# def convert(date_time):
#     format = '%b %d %Y %I:%M%p'
#     datetime_str = datetime.strptime(date_time, format)
#
#     return datetime_str
#
# print(convert('Jan 1 2014 2:43PM'))

# ------------------------------------------

"""
4. Write a Python program to get the current time in Python.
Sample Format :  13:19:49.078205
"""
# print(datetime.now().time())

# ------------------------------------------

"""
5. Write a Python program to subtract five days from current date.
Sample Date :
Current Date : 2015-06-22
5 days before Current Date : 2015-06-17
"""
# sub_day = 5
# curr_date = date.today()
# new_date = curr_date - timedelta(5)
# print(new_date)

# ------------------------------------------

"""
6. Write a Python program to convert unix timestamp string to readable date.
Sample Unix timestamp string : 1284105682
Expected Output : 2010-09-10 13:31:22
"""

# utc_timestamp = 1284105682
# print(datetime.utcfromtimestamp(utc_timestamp))

# ------------------------------------------

"""
7. Write a Python program to print yesterday, today, tomorrow.
"""
# print('today: ', date.today())
# print('yesterday: ', date.today() - timedelta(1))
# print('Tomorrow: ', date.today() + timedelta(1))

# ------------------------------------------

"""
8. Write a Python program to convert the date to datetime (midnight of the date) in Python.
Sample Output : 2015-06-22 00:00:00
"""
# print(datetime.combine(date.today(), datetime.min.time()))

# ------------------------------------------

"""
9. Write a Python program to print next 5 days starting from today.
"""
# for i in range(5):
#     print(date.today() + timedelta(i))
#

# ------------------------------------------

"""
10. Write a Python program to add 5 seconds with the current time.
Sample Data :
13:28:32.953088
13:28:37.953088
"""
# print(datetime.now())
# print(datetime.now() + timedelta(0, 5))

# ------------------------------------------

"""
11. Write a Python program to convert Year/Month/Day to Day of Year in Python.
"""
# dt = datetime.now()
# print(dt.timetuple().tm_yday)

# ------------------------------------------

"""
12. Write a Python program to get current time in milliseconds in Python
"""
# dt = datetime.now()
# print(dt.timestamp())

# ------------------------------------------

"""
13. Write a Python program to get week number.
Sample Date : 2015, 6, 16
Expected Output : 25
"""
# print(date.today().strftime("%V"))

# ------------------------------------------

"""
14. Write a Python program to find the date of the first Monday of a given week.
Sample Year and week : 2015, 50
Expected Output : Mon Dec 14 00:00:00 2015
"""
# dt = datetime.strptime('2015 50 1', '%Y %W %w')
# print(datetime.ctime(dt))

# ------------------------------------------

"""
15. Write a Python program to select all the Sundays of a specified year.
"""
# def count_sunday(date):
#     date_str = datetime.strptime(date, '%d %b  %Y')
#     for i in range(0, 365):
#         dt = date_str + timedelta(i)
#         if dt.weekday() == 6:
#             print('Sunday: ', dt)
# count_sunday('1 Jan 2022')

# ------------------------------------------

"""
16. Write a Python program to add year(s) with a given date and display the new date.

Sample Data : (addYears is the user defined function name)
print(addYears(datetime.date(2015,1,1), -1))
print(addYears(datetime.date(2015,1,1), 0))
print(addYears(datetime.date(2015,1,1), 2))
print(addYears(datetime.date(2000,2,29),1))
"""
# def addYears(d, years):
#     try:
#         return d.replace(year=d.year + years)
#     except ValueError:
#         return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))
#
#
# print(addYears(date(2015, 1, 1), -1))
# print(addYears(date(2015, 1, 1), 0))
# print(addYears(date(2015, 1, 1), 2))
# print(addYears(date(2000, 2, 29), 1))

# ------------------------------------------


"""
17. Write a Python program to drop microseconds from datetime.
"""
# print(datetime.today().replace(microsecond=0))

# ------------------------------------------


"""
18. Write a Python program to get days between two dates.
Sample Dates : 2000,2,28, 2001,2,28
Expected Output : 366 days, 0:00:00
"""
# a = date(2000, 2, 28)
# b = date(2001, 2, 28)
# c = b - a
# print(c)

# ------------------------------------------


"""
19. Write a Python program to get the date of the last Tuesday.
"""
# today = date.today()
# offset = (today.weekday() - 1) % 7
# last_tuesday = today - timedelta(days=offset)
# print(last_tuesday)
#

# ------------------------------------------

"""
20. Write a Python program to test the third Tuesday of a month.
"""
# def is_third_tuesday(s):
#     d = datetime.strptime(s, '%b %d, %Y')
#     return d.weekday() == 1 and 14 < d.day < 22
#
# print(is_third_tuesday('Jun 23, 2015')) #False
# print(is_third_tuesday('Jun 16, 2015')) #True
# print(is_third_tuesday('Jul 21, 2015')) #False

# ------------------------------------------
