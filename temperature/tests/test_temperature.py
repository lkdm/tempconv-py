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
        # Reduces verbosity of code
        def runTest(C, K):
            self.assertEqual(K, self.temperature._celsiusToKelvin(C))
        
        runTest(373.15, 100)
        runTest(173.15, -100)
        # runTest(0, 273.15)
        runTest(-100, 173.15)
        runTest(-273.15, 0)

if __name__ == '__main__':
    # if test is being run directly
    unittest.main()
