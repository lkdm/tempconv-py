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
		return 5/9 * (F - 32) + 273
	def __kelvinToFahrenheit(self, K):
		return 9/5 * (K - 273) + 32

	'''
	Private checks if temperature obeys laws of physics
	'''
	def __makeLegalTemperature(self, K):
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
		self.kelvin = self.__makeLegalTemperature(self.__celsiusToKelvin(C))
	@celsius.getter
	def celsius(self):
		# Retrieves Celsius from Kelvin
		return self.__kelvinToCelsius(self.kelvin)

	'''
	Handles Fahrenheit as Kelvin
	'''
	@property
	def fahrenheit(self):
		pass
	@fahrenheit.setter
	def fahrenheit(self, F):
		# Stores Fahrenheit as Kelvin 
		self.kelvin = self.__makeLegalTemperature(self.__fahrenheitToKelvin(F))
	@fahrenheit.getter
	def fahrenheit(self):
		# Retrieves Fahrenheit from Kelvin
		return self.__kelvinToFahrenheit(self.kelvin)
	'''
	TODO: Write unit testing functions
	'''
	
		
t = Temperature()
# Fix Kelvin error check not working
t.kelvin = -10 
print(t.kelvin)
