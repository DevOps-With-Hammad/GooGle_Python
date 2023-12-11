# Seconds to hours converter.

def second_to_hours(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


total = input("please enter your converted value ")
hours, minutes, remaining_seconds =second_to_hours(int(total))
print(hours, minutes, remaining_seconds)

for second_to_hours in range (0, 10):
    print(hours, minutes, remaining_seconds)
