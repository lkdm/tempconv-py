'''
Imports
'''
import unittest
import sys
sys.path.append('../')
import temperature

from decimal import *

class TestTemperatureMethods(unittest.TestCase):



    # Ensures temperatures round to two places. Exists here because test cases are passed into runTest() as a Float.
    def _round(self, number):
        getcontext().prec = 6
        return Decimal(number).quantize(Decimal('.01'), rounding=ROUND_HALF_EVEN)

    # Compares input to testcase, and rounds | Exists to lessen verbosity
    def _compare(self, input, testcase):
        self.assertEqual(input, self._round(testcase))

    # Each test, constructs new temperature object        
    def setUp(self):
        self.temperature = temperature.Temperature()

    '''
    Tests conversion methods.
    Each has a runTest(), to reduce verbosity of code
    '''

    def test__celsiusToKelvin(self):
        def runTest(C, K):
            self._compare(self.temperature._celsiusToKelvin(Decimal(C)), K)
        
        runTest(100, 373.15)
        runTest(0, 273.15)

    def test__kelvinToCelsius(self):
        def runTest(K, C):
            self._compare(self.temperature._kelvinToCelsius(Decimal(K)), C)

        runTest(0, -273.15)
        runTest(1389.381, 1116.23)

    def test__fahrenheitToKelvin(self):
        def runTest(F, K):
            self._compare(self.temperature._fahrenheitToKelvin(Decimal(F)), K)

        runTest(0, 255.37)
        runTest(-459.67, 0)
        runTest(838.32, 721.11)

    def test__kelvinToFahrenheit(self):
        def runTest(K, F):
            self._compare(self.temperature._kelvinToFahrenheit(Decimal(K)), F)

        runTest(0, -459.67)
        runTest(255.37, 0)

    def test__rankineToKelvin(self):
        def runTest(Ra, K):
            self._compare(self.temperature._rankineToKelvin(Decimal(Ra)), K)

        runTest(153, 85)
        runTest(100, 55.56)

    def test__kelvinToRankine(self):
        def runTest(K, Ra):
            self._compare(self.temperature._kelvinToRankine(Decimal(K)), Ra)

        runTest(15, 27)
        runTest(100, 180)

    def test__romerToKelvin(self):
        def runTest(Ro, K):
            self._compare(self.temperature._romerToKelvin(Decimal(Ro)), K)

        runTest(21.6, 300.01)

    def test__kelvinToRomer(self):
        def runTest(K, Ro):
            self._compare(self.temperature._kelvinToRomer(Decimal(K)), Ro)

        runTest(180, -41.40)

    def test__reaumurToKelvin(self):
        def runTest(Re, K):
            self._compare(self.temperature._reaumurToKelvin(Decimal(Re)), K)

        runTest(125, 429.40)

    def test__kelvinToReaumur(self):
        def runTest(K, Re):
            self._compare(self.temperature._kelvinToReaumur(Decimal(K)), Re)

        runTest(180, -74.52)


if __name__ == '__main__':
    # if test is being run directly
    unittest.main()
