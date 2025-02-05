seconds = int(input("Enter Length of Time in Seconds: "))

seconds_per_year = 365*24*60*60
year = seconds // seconds_per_year
seconds = seconds - (year * seconds_per_year)

seconds_per_day = 24*60*60
days = seconds // seconds_per_day
seconds = seconds - (days * seconds_per_day)

seconds_per_hour = 60*60
hours = seconds // seconds_per_hour
seconds = seconds - (hours*seconds_per_hour)

seconds_per_minute = 60
minutes = seconds // seconds_per_minute
seconds = seconds - (minutes * seconds_per_minute)

print("years: ", year)
print("days: " , days)
print("hours: ", hours)
print("minutes: ", minutes)
print("seconds: ", seconds)