"""
H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). Determine the angle
(in degrees) of the hour hand on the clock face right now.
In all the problems input the data using input() and print the result using print().
"""

hours = float(input("hours"))
minutes = float(input("minutes"))
seconds = float(input("seconds"))

one_hour_degrees = 360 / 12
one_minute_degrees = one_hour_degrees / 60
one_second_degrees = one_minute_degrees / 60

print(one_hour_degrees * hours + one_minute_degrees * minutes + one_second_degrees * seconds)