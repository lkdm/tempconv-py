import sys
sys.path.append('../')

import temperature

t = temperature.Temperature()

t.celsius = 100

print(t.fahrenheit)