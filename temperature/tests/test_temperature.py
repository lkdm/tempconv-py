'''
Imports
'''
import unittest
import sys
sys.path.append('../')
import temperature

from decimal import *


'''
Because floats introduce miniscule inaccuracies,
it's important that we round to two places when comparing.
'''
TWOPLACES = Decimal(10) ** -2 #same as Decimal('0.01')
def _round(rawTemperature):
    return Decimal(rawTemperature).quantize(TWOPLACES)

class TestTemperatureMethods(unittest.TestCase):

    

    # Each test, constructs new temperature object        
    def setUp(self):
        self.temperature = temperature.Temperature()



    def test__celsiusToKelvin(self):

        self.assertEqual(100, _round(100))

        # Reduces verbosity of code
        def test(C, K):
            self.assertEqual(Decimal(C), _round(self.temperature._celsiusToKelvin(K)))
        
        test(373.15, 100)
        test(173.15, -100)

if __name__ == '__main__':
    # if test is being run directly
    unittest.main()
