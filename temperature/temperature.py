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
	Ensures that temperature is returned with two decimal places
	'''
	def _round(self, number):
		# Precision includes all digits, not just after decimal point.
		getcontext().prec = 6
		return Decimal(number).quantize(Decimal('.01'), rounding=ROUND_HALF_EVEN)

	'''
	Private Kelvin/Celsius conversions
	'''
	def _celsiusToKelvin(self, C):
		return self._round(Decimal(C) + Decimal(273.15))
	def _kelvinToCelsius(self, K):
		return self._round(Decimal(K) - Decimal(273.15))
	'''
	Private Fahrenheit/Kelvin conversions
	'''
	def _fahrenheitToKelvin(self, F):
		return self._round((Decimal(F) - Decimal(32)) / Decimal(1.8) + Decimal(273.15))
	def _kelvinToFahrenheit(self, K):
		return self._round((Decimal(K) - Decimal(273.15)) * Decimal(1.8) + Decimal(32))
	'''
	Handles Celsius as Kelvin
	'''
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

	'''
	Handles Fahrenheit as Kelvin
	'''
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
