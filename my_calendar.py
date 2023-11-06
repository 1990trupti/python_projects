import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the Month: "))

calendar.setfirstweekday(calendar.SUNDAY)
my_calendar = calendar.month(year,month)

my_cal = calendar.calendar(year)
print(my_calendar)
# print(my_cal)
















