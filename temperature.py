# Temperature library

# Store as Kelvin

class Temperature:
	'''
	Temperature is always stored as Kelvin
	'''
	def __init__(self):
		pass
	'''
	Private Kelvin/Celsius conversions
	'''
	def __celsiusToKelvin(self, C):
		return C + 273
	def __kelvinToCelsius(self, K):
		return K - 273
	'''
	Private Fahrenheit/Kelvin conversions
	'''
	def __fahrenheitToKelvin(self, F):
		return 5/9 (F - 32) + 273
	def __kelvinToFahrenheit(self, K):
		return 9/5 (K - 273) + 32

	'''
	Also store Celsius as Kelvin
	'''
	@property
	def celsius(self):
		return self._celsius
	@celsius.setter
	def celsius(self, C):
		# Stores Kelvin & Celsius
		self._celsius = C
		self._kelvin = self.__celsiusToKelvin(C)
		print(self.__celsiusToKelvin(C))
	@celsius.getter
	def celsius(self):
		# Retrieves Celsius from Kelvin
		return self.__kelvinToCelsius(self._kelvin)

	'''
	TODO: Duplicate above code for Fahrenheit
	'''

	'''
	Testing functions
	'''
	
		
t = Temperature()
t._kelvin = 100
print(t.celsius)
