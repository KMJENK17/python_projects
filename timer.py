import time
import datetime

# Inputs for the timer
h = input('Enter the time in hours: ')
m = input('Enter the time in minutes: ')
s = input('Enter the time in seconds:')

# Timer class
def countdown(h, m, s):
    total_seconds = h * 3600 + m * 60 + s

    while total_seconds > 0:

        timer = datetime.timedelta(seconds = total_seconds)

        print(timer, end='\r')

        time.sleep(1)

        total_seconds -= 1

    print('DONE')

countdown(int(h), int(m), int(s))