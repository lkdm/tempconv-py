# Temperature library

from decimal import *

class Temperature:
	'''
	Temperature is always stored as Kelvin
	'''
	def __init__(self):
		pass
	
	'''
	Private Kelvin/Celsius conversions
	'''
	def _celsiusToKelvin(self, C):
		return round(C + 273.15, 2)
	def _kelvinToCelsius(self, K):
		return K - 273.15
	'''
	Private Fahrenheit/Kelvin conversions
	'''
	def _fahrenheitToKelvin(self, F):
		return 5/9 * (F - 32) + 273
	def _kelvinToFahrenheit(self, K):
		return 9/5 * (K - 273) + 32

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
