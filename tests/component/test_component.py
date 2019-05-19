import unittest
import HumanCalculator

class TestCalcComponent(unittest.TestCase):
    def setUp(self):
        self.calc = HumanCalculator.HumanCalc()
    
    def test_operations(self):
        inputted = [
            '3 + 3 - 7',
            '20 / 5 = 2 * 2',
        ]
        expected = ['three plus three minus seven', 'twenty divide by five equals two multiply by two']
        returned = [self.calc.convert(inp) for inp in inputted]
        self.assertEqual(returned, expected)

    def test_handling_small_numbers(self):
        inputted = map(str, [0, 3, 12, 18, 35, 79, 88, 100, 116, 149, 200, 345, 999, 1000, 1001, 1010])
        returned = list(map(self.calc.convert, inputted))
        expected = ['zero', 'three', 'twelve', 'eighteen', 'thirty-five', 'seventy-nine', 'eighty-eight',
        'one hundred', 'one hundred sixteen', 'one hundred forty-nine', 'two hundreds', 
        'three hundreds forty-five', 'nine hundreds ninety-nine', 'one thousand', 'one thousand one', 'one thousand ten']
        self.assertEqual(returned, expected)

    def test_handling_big_numbers(self):
        inputted = map(str, [10000, 1000000, 1000000000, 1000100100, 1000100100100, 100000000000000])
        returned = list(map(self.calc.convert, inputted))
        expected = ['ten thousands', 'one million', 'one billion', 'one billion one hundred thousands one hundred',
            'one trillion one hundred millions one hundred thousands one hundred', 'one hundred trillions']
        self.assertEqual(returned, expected)