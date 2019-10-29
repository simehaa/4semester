import calendar
y = int(raw_input("yyyy = "))
m = int(raw_input("mm = "))
d = int(raw_input("dd = "))
print calendar.day_name[calendar.weekday(y, m, d)]
