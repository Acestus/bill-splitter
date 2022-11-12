first_hours = int(input())
first_minutes = int(input())
first_seconds = int(input())
second_hours = int(input())
second_minutes = int(input())
second_seconds = int(input())
SECONDS_IN_HOUR = 3600
first_seconds += first_minutes * 60 + first_hours * SECONDS_IN_HOUR
second_seconds += second_minutes * 60 + second_hours * SECONDS_IN_HOUR
difference = abs(first_seconds - second_seconds)
print(difference)
