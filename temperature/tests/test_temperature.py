'''
Imports
'''
import unittest
import sys
sys.path.append('../')
import temperature

class TestTemperatureMethods(unittest.TestCase):

    # Each test, constructs new temperature object        
    def setUp(self):
        self.temperature = temperature.Temperature()

    def test__celsiusToKelvin(self):
        self.assertEqual(373.15, self.temperature._celsiusToKelvin(100))
        self.assertEqual(173.15, self.temperature._celsiusToKelvin(-100))

if __name__ == '__main__':
    # if test is being run directly
    unittest.main()
