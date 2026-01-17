"""
Calculate current age and total days passed since birth using the time module.
"""

import time

# Input birthdate from user
birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")

# Parse input to get year, month, day
birth_year, birth_month, birth_day = map(int, birthdate_input.split("-"))

# Get current time
current_time = time.localtime()
current_year = current_time.tm_year
current_month = current_time.tm_mon
current_day = current_time.tm_mday

# Calculate age in years
age_years = current_year - birth_year
if (current_month, current_day) < (birth_month, birth_day):
    age_years -= 1  # Birthday not yet reached this year

# Calculate total days since birth
birth_seconds = time.mktime((birth_year, birth_month, birth_day, 0, 0, 0, 0, 0, -1))
current_seconds = time.mktime(current_time)
total_days = int((current_seconds - birth_seconds) / (24 * 3600))

# Display results
print(f"Your current age is {age_years} years.")
print(f"Total days passed since your birth: {total_days}")
