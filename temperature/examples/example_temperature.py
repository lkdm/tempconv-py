'''
usage_temperature.py

This script shows an example of usage for temperature.py
'''

import sys
sys.path.append('../')
import temperature

t = temperature.Temperature()

DEGREES = "°"
DEGREES_C = DEGREES + "C"
DEGREES_F = DEGREES + "F"
KELVINS = "K"

t.fahrenheit = 100
print(str(t.celsius) + DEGREES_C)

# an f-string can also be used to avoid the need to use str()
# print(f'{t.celsius}{DEGREES_C}')
