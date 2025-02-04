seconds_per_day = float(input("Enter Length of Time in Seconds: "))
seconds_per_year = 360*24*60*60
year = float(input(seconds/seconds_per_year))
seconds_left = float(input(seconds%seconds_per_year))
seconds_per_day = 24*60*60
days = float(input(seconds_left/seconds_per_day))
seconds_left = float(input(seconds_left%seconds_per_day))
seconds_per_hour = 60*60
hours = float(input(seconds_left/seconds_per_hour))
seconds_left = float(input(seconds_left%seconds_per_hour))
minutes = float(input(seconds_left/60))
seconds = float(input(seconds_left%60))

print("years: " + year)
print("days: " + days)
print("hours: " + hours)
print("minutes: " + minutes)
print("seconds: " + seconds)