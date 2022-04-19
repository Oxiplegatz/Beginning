from datetime import datetime

# Datetime intro
birthday = datetime(1984, 12, 24, 5, 33, 15)

print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.hour)
print(birthday.minute)
print(birthday.second)
print(birthday.weekday())

# Datetime timedelta
one_year = datetime(2022, 1, 1) - datetime(2021, 1, 1)
print(one_year)

time_passed = datetime.now() - datetime(2022, 1, 1)
print(time_passed)

utc_time = datetime.utcnow()
print(utc_time)


# .strptime function
parsed_date = datetime.strptime('March 21, 2022', '%B %d, %Y')
print(parsed_date)
print(parsed_date.month)
print(parsed_date.year)
print(parsed_date.day)

# .strftime function
date_string = datetime.strftime(datetime.now(), '%B %d, %Y')
print(date_string)
