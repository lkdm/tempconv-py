'''
temperature.py

The easiest standalone temperature conversion library
Author	https://github.com/luknuk
'''

# We use decimal rather than Float, because Floats are never accurate.
from decimal import *

class Temperature:
    '''
    Temperature is always stored as Kelvin
    '''
    def __init__(self):
        pass
    '''
    Ensures temperatures round to two decimal places.
    '''
    def _round(self, number):
        # Precision includes all digits, not just after decimal point.
        getcontext().prec = 6
        return Decimal(number).quantize(Decimal('.01'), rounding=ROUND_HALF_EVEN)

    '''
    Conversion methods. These do the actual conversion.
    '''
    def _celsiusToKelvin(self, C):
        return self._round(Decimal(C) + Decimal(273.15))
    def _kelvinToCelsius(self, K):
        return self._round(Decimal(K) - Decimal(273.15))
    def _fahrenheitToKelvin(self, F):
        return self._round((Decimal(F) - Decimal(32)) / Decimal(1.8) + Decimal(273.15))
    def _kelvinToFahrenheit(self, K):
        return self._round((Decimal(K) - Decimal(273.15)) * Decimal(1.8) + Decimal(32))
    def _rankineToKelvin(self, Ra):
        return self._round((Decimal(Ra) * ((Decimal(5) / Decimal(9)))))
    def _kelvinToRankine(self, K):
        return self._round(Decimal(K) * Decimal(1.8))

    '''
    Syntactic sugar methods. These allow the conversion to happen in the background.
    '''
    # Getters & Setters to handle Celsius as Kelvin
    @property
    def celsius(self):
        pass
    @celsius.setter
    def celsius(self, C):
        # Stores Celsius as Kelvin
        self.kelvin = self._celsiusToKelvin(C)
    @celsius.getter
    def celsius(self):
        # Retrieves Celsius from Kelvin
        return self._kelvinToCelsius(self.kelvin)

    # Getters & Setters to handle Fahrenheit as Kelvin
    @property
    def fahrenheit(self):
        pass
    @fahrenheit.setter
    def fahrenheit(self, F):
        # Stores Fahrenheit as Kelvin 
        self.kelvin = self._fahrenheitToKelvin(F)
    @fahrenheit.getter
    def fahrenheit(self):
        # Retrieves Fahrenheit from Kelvin
        return self._kelvinToFahrenheit(self.kelvin)

    # Getters & Setters to handle Rankine as Kelvin
    @property
    def rankine(self):
        pass
    @rankine.setter
    def rankine(self, Ra):
        # Stores Rankine as Kelvin
        self.kelvin = self._rankineToKelvin(Ra)
    @rankine.getter
    def rankine(self):
        # Retrieves Rankine from Kelvin
        return self._kelvinToRankine(self.kelvin)

# Thanks for reading :)
