'''
usage_temperature.py

This script shows an example of usage for temperature.py
'''

import sys
sys.path.append('../')
import temperature

t = temperature.Temperature()

DEGREES = "°"

t.fahrenheit = 100
print(str(t.celsius) + DEGREES + " C")
