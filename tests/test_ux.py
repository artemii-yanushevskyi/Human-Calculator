import unittest
import HumanCalculator

class TestCalcUX(unittest.TestCase):
    def setUp(self):
        self.calc = HumanCalculator.HumanCalc()
    
    def test_text_consistency(self):
        expected = 'thirty-four billions three hundreds forty-three millions six hundreds forty-three thousands '\
            'two hundreds thirty-four divide by thirty-five thousands three hundreds forty-four plus forty-three millions '\
                'two hundreds forty-five thousands three hundreds forty-three equals thirty-four thousands two hundreds thirty-three'
        self.assertEqual(self.calc.convert('34343643234 / 35344 + 43245343 = 34233'), expected)

    def test_handling_zeroes(self):
        expected = 'ten billions three millions two thousands four divide by three '\
            'thousands plus zero equals two trillions two billions thirty thousands four hundreds four'
        self.assertEqual(self.calc.convert('10003002004 / 3000 + 0000 = 002002000030404'), expected)
    
    def test_handling_anomalous_spaces(self):
        expected = 'one hundred four divide by forty-five plus three minus twenty-three equals '\
            'four equals five minus twenty-two divide by three minus twenty-three'
        self.assertEqual(self.calc.convert('104   /   45+3- 23 = 4=5 -  22/3 - 23'), expected)