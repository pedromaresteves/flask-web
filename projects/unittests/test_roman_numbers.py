import unittest
from projects.roman import convert_to_roman
# IMPORTANT:
# All test functions must start with test_
# unittest Assertion Methods: https://docs.python.org/3/library/unittest.html#assert-methods


class GuessNumber(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Use setUpClass to run code at the beginning of the test Suite
        pass

    @classmethod
    def tearDownClass(cls):
        # Use tearDownClass to run code at the end of the test Suite
        pass

    def setUp(self):
        # Use setUp function to run code before each test case
        pass

    def tearDown(self):
        # Use setUp function to run code after each test case
        pass

    def test_0(self):
        result = convert_to_roman(0)
        self.assertFalse(result['value'])
    def test_1(self):
        result = convert_to_roman(1)
        self.assertEqual(result['value'], "I")
    def test_2(self):
        result = convert_to_roman(2)
        self.assertEqual(result['value'], "II")
    def test_3(self):
        result = convert_to_roman(3)
        self.assertEqual(result['value'], "III")
    def test_4(self):
        result = convert_to_roman(4)
        self.assertEqual(result['value'], "IV")
    def test_5(self):
        result = convert_to_roman(5)
        self.assertEqual(result['value'], "V")
    def test_6(self):
        result = convert_to_roman(6)
        self.assertEqual(result['value'], "VI")
    def test_7(self):
        result = convert_to_roman(7)
        self.assertEqual(result['value'], "VII")
    def test_8(self):
        result = convert_to_roman(8)
        self.assertEqual(result['value'], "VIII")
    def test_9(self):
        result = convert_to_roman(9)
        self.assertEqual(result['value'], "IX")
    def test_10(self):
        result = convert_to_roman(10)
        self.assertEqual(result['value'], "X")
    def test_11(self):
        result = convert_to_roman(11)
        self.assertEqual(result['value'], "XI")
    def test_12(self):
        result = convert_to_roman(12)
        self.assertEqual(result['value'], "XII")
    def test_13(self):
        result = convert_to_roman(13)
        self.assertEqual(result['value'], "XIII")
    def test_14(self):
        result = convert_to_roman(14)
        self.assertEqual(result['value'], "XIV")
    def test_15(self):
        result = convert_to_roman(15)
        self.assertEqual(result['value'], "XV")
    def test_16(self):
        result = convert_to_roman(16)
        self.assertEqual(result['value'], "XVI")
    def test_17(self):
        result = convert_to_roman(17)
        self.assertEqual(result['value'], "XVII")
    def test_18(self):
        result = convert_to_roman(18)
        self.assertEqual(result['value'], "XVIII")
    def test_19(self):
        result = convert_to_roman(19)
        self.assertEqual(result['value'], "XIX")
    def test_20(self):
        result = convert_to_roman(20)
        self.assertEqual(result['value'], "XX")
    def test_30(self):
        result = convert_to_roman(30)
        self.assertEqual(result['value'], "XXX")
    def test_40(self):
        result = convert_to_roman(40)
        self.assertEqual(result['value'], "XL")
    def test_50(self):
        result = convert_to_roman(50)
        self.assertEqual(result['value'], "L")
    def test_60(self):
        result = convert_to_roman(60)
        self.assertEqual(result['value'], "LX")
    def test_70(self):
        result = convert_to_roman(70)
        self.assertEqual(result['value'], "LXX")
    def test_80(self):
        result = convert_to_roman(80)
        self.assertEqual(result['value'], "LXXX")
    def test_90(self):
        result = convert_to_roman(90)
        self.assertEqual(result['value'], "XC")
    def test_100(self):
        result = convert_to_roman(100)
        self.assertEqual(result['value'], "C")
    def test_200(self):
        result = convert_to_roman(200)
        self.assertEqual(result['value'], "CC")
    def test_300(self):
        result = convert_to_roman(300)
        self.assertEqual(result['value'], "CCC")
    def test_400(self):
        result = convert_to_roman(400)
        self.assertEqual(result['value'], "CD")
    def test_500(self):
        result = convert_to_roman(500)
        self.assertEqual(result['value'], "D")
    def test_600(self):
        result = convert_to_roman(600)
        self.assertEqual(result['value'], "DC")
    def test_700(self):
        result = convert_to_roman(700)
        self.assertEqual(result['value'], "DCC")
    def test_800(self):
        result = convert_to_roman(800)
        self.assertEqual(result['value'], "DCCC")
    def test_900(self):
        result = convert_to_roman(900)
        self.assertEqual(result['value'], "CM")
    def test_1000(self):
        result = convert_to_roman(1000)
        self.assertEqual(result['value'], "M")
    def test_2000(self):
        result = convert_to_roman(2000)
        self.assertEqual(result['value'], "MM")
    def test_1111(self):
        result = convert_to_roman(1111)
        self.assertEqual(result['value'], "MCXI")
    def test_4444(self):
        result = convert_to_roman(4444)
        self.assertEqual(result['value'], "MMMMCDXLIV")
    def test_9999(self):
        result = convert_to_roman(9999)
        self.assertEqual(result['value'], "MMMMMMMMMCMXCIX")
    def test_1984(self):
        result = convert_to_roman(1984)
        self.assertEqual(result['value'], "MCMLXXXIV")



# With the below function we can run the tests with 'python test_guess_number.py'
# Without this function we would have to do 'python -m unittest test_guess_number.py'
if __name__ == '__main__':
    unittest.main()