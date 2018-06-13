t = 1.0e9
seconds_in_year = (60*60*24*365.25)
y = int(t)/int(seconds_in_year)
m = t/((t%int(seconds_in_year))*12)
print y, m
