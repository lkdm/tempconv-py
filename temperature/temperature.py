# Temperature library

# Store as Kelvin

class Temperature:
	'''
	Temperature is always stored as Kelvin
	'''
	def __init__(self):
		pass


	def _test(self):
		return True
	
	'''
	Private Kelvin/Celsius conversions
	'''
	def _celsiusToKelvin(self, C):
		return C + 273.15
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
	Private checks if temperature obeys laws of physics
	'''
	def _makeLegalTemperature(self, K):
		# TODO: Ensure type is int, float, or double
		if K < 0:
			return 0
		else:
			return K

	'''
	Handles Celsius as Kelvin
	'''
	@property
	def celsius(self):
		pass
	@celsius.setter
	def celsius(self, C):
		# Stores Kelvin & Celsius
		self.kelvin = self._makeLegalTemperature(self._celsiusToKelvin(C))
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
		self.kelvin = self._makeLegalTemperature(self._fahrenheitToKelvin(F))
	@fahrenheit.getter
	def fahrenheit(self):
		# Retrieves Fahrenheit from Kelvin
		return self._kelvinToFahrenheit(self.kelvin)
