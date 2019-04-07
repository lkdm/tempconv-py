'''
temperature.py

The easiest standalone temperature conversion library
Author	https://github.com/luknuk
'''

# We use decimal rather than Float, because Floats are never accurate.
from decimal import Decimal
from decimal import getcontext
from decimal import ROUND_HALF_EVEN

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
    def _romerToKelvin(self, Ro):
        return self._round(((Decimal(Ro) - Decimal(7.5)) * Decimal(40) / Decimal(21)) + Decimal(273.15))
    def _kelvinToRomer(self, K):
        return self._round(((Decimal(K) - Decimal(273.15)) * (Decimal(21) / Decimal(40))) + Decimal(7.5))
    def _reaumurToKelvin(self, Re):
        return self._round((Decimal(Re) * Decimal(1.25)) + Decimal(273.15))
    def _kelvinToReaumur(self, K):
        return self._round((Decimal(K) - Decimal(273.15)) * Decimal(0.8))
    def _delisleToKelvin(self, D):
        return self._round(Decimal(373.15) - D * Decimal(2) / Decimal(3))
    def _kelvinToReaumur(self, K):
        return self._round((Decimal(373.15) - K) * (Decimal(3) / Decimal(2)))

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

    # Getters & Setters to handle Romer as Kelvin
    @property
    def romer(self):
        pass
    @romer.setter
    def romer(self, Ro):
        # Stores Romer as Kelvin
        self.kelvin = self._romerToKelvin(Ro)
    @romer.getter
    def romer(self):
        # Retrieves Romer from Kelvin
        return self._kelvinToRomer(self.kelvin)

    # Getters & Setters to handle Reaumur as Kelvin
    @property
    def reaumur(self):
        pass
    @reaumur.setter
    def reaumur(self, Re):
        # Stores Reaumur as Kelvin
        self.kelvin = self._reaumurToKelvin(Re)
    @reaumur.getter
    def reaumur(self):
        # Retrieves Reaumur from Kelvin
        return self._kelvinToReaumur(self.kelvin)

    # Getters & Setters to handle Delisle as Kelvin
    @property
    def Delisle(self):
        pass
    @Delisle.setter
    def Delisle(self, D):
        # Stores Delisle as Kelvin
        self.kelvin = self._delisleToKelvin(D)
    @Delisle.getter
    def Delisle(self):
        # Retrieves Delisle from Kelvin
        return self._kelvinToReaumur(self.kelvin)

# Thanks for reading :)
