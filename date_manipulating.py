# Getting the Current Date and Time

from datetime import datetime, date, timedelta

now = datetime.now()
print("Current timestamp:", now)

today = datetime.today()
print("Today's Date:", today)


# Creating Specific Dates
specific_date = date(2025, 12, 25)  # Specific date: date(year, month, day)

# Specific datetime: datetime(year, month, day, hour, minute, second)
specific_datetime = datetime(2025, 12, 18, 14, 11, 30)

print(specific_date)
print(specific_datetime)

# Date Arithmetic with
today = date.today()

# add 5 days
future_date = today + timedelta(days=5)
print(future_date)

# subtract 2 weeks days
past_date = today - timedelta(weeks=2)
print(past_date)

# Calculate the difference between two date
days_between = future_date - today
print(days_between.days)

now = datetime.now()
formated_str = now.strftime("%Y-%m-%d %H:%M:%S")

print("Formated:", formated_str)

date_string = "25/12/2025"
parse_date = datetime.strptime(date_string, "%d/%m/%Y")
print("Parsed object: ", parse_date)

