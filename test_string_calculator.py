import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty_string(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number(self):
        self.assertEqual(self.calculator.add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(self.calculator.add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(self.calculator.add("1,2,3,4,5"), 15)

    def test_newline_delimiter(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(self.calculator.add("//;\n1;2"), 3)

    def test_negative_number_exception(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,3,-4")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2, -4")

    def test_ignore_numbers_greater_than_1000(self):
        self.assertEqual(self.calculator.add("2,1001"), 2)

    def test_custom_delimiter_of_any_length(self):
        self.assertEqual(self.calculator.add("//[***]\n1***2***3"), 6)

    def test_multiple_custom_delimiters(self):
        self.assertEqual(self.calculator.add("//[*][%]\n1*2%3"), 6)

    def test_multiple_custom_delimiters_with_length_longer_than_one_char(self):
        self.assertEqual(self.calculator.add("//[***][%%%]\n1***2%%%3"), 6)

if __name__ == "__main__":
    unittest.main()
