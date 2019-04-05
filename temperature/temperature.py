# Temperature library
# todo: Add formatting method

from decimal import *

class Temperature:
	'''
	Temperature is always stored as Kelvin
	'''
	def __init__(self):
		pass
	'''
	Private method. Ensures temperatures round to two decimal places.
	'''
	def _round(self, number):
		# Precision includes all digits, not just after decimal point.
		getcontext().prec = 6
		return Decimal(number).quantize(Decimal('.01'), rounding=ROUND_HALF_EVEN)

	'''
	Conversion methods. These do the heavy lifting.
	'''
	def _celsiusToKelvin(self, C):
		return self._round(Decimal(C) + Decimal(273.15))
	def _kelvinToCelsius(self, K):
		return self._round(Decimal(K) - Decimal(273.15))
	def _fahrenheitToKelvin(self, F):
		return self._round((Decimal(F) - Decimal(32)) / Decimal(1.8) + Decimal(273.15))
	def _kelvinToFahrenheit(self, K):
		return self._round((Decimal(K) - Decimal(273.15)) * Decimal(1.8) + Decimal(32))
	
	'''
	Syntactic sugar methods. Used to do conversion in background.
	'''
	# Getters & Setters to handle Celsius as Kelvin
	@property
	def celsius(self):
		pass
	@celsius.setter
	def celsius(self, C):
		# Stores Kelvin & Celsius
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
