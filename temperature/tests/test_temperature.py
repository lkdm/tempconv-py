'''
Imports
'''
import unittest
import sys
sys.path.append('../')
import temperature

from decimal import *

class TestTemperatureMethods(unittest.TestCase):

    '''
    _round exists because arguments are passed into runTest as a float.
	This method parallels _round in temperature class. To clean up the code, they should be merged
    '''
    def _round(self, number):
        getcontext().prec = 6
        return Decimal(number).quantize(Decimal('.01'), rounding=ROUND_HALF_EVEN)

    # Each test, constructs new temperature object        
    def setUp(self):
        self.temperature = temperature.Temperature()

    def test__celsiusToKelvin(self):
        # Reduces verbosity of code
        def runTest(K, C):
            self.assertEqual(self._round(K), self.temperature._celsiusToKelvin(Decimal(C)))
        
        runTest(373.15, 100)
        runTest(173.15, -100)
        runTest(0, -273.15)

if __name__ == '__main__':
    # if test is being run directly
    unittest.main()
