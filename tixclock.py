from __future__ import print_function
import os
import datetime
import random
import time
import sys

def get_time():
    now = datetime.datetime.now()
    hours_1, hours_2 = divmod(now.hour, 10)
    minutes_1, minutes_2 = divmod(now.minute, 10)
    return hours_1, hours_2, minutes_1, minutes_2

def shuffle_string(points):
    l = list(points)
    random.shuffle(l)
    shuffled = ''.join(l)
    return shuffled

def display_fields(number_of_fields, value):
    points = ''
    points += value * 'o'
    points += (number_of_fields - value) * '.'
    points = shuffle_string(points)

    for i in range(0, number_of_fields):
        if i%3 == 0:
            print()
        print(points[i], end=" ")
    print()

def main():
    hours_1, hours_2, minutes_1, minutes_2 = get_time()

    os.system('setterm -cursor off')
    while True:
        try:
            os.system('clear')
            display_fields(3, hours_1)
            display_fields(9, hours_2)
            display_fields(9, minutes_1)
            display_fields(9, minutes_2)
            time.sleep(10)
        except KeyboardInterrupt:
            os.system('clear')
            os.system('setterm -cursor on')
            sys.exit()

if __name__ == '__main__':
    main()
