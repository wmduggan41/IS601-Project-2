import unittest
import TestFiles

from Calculator import Calculator
from StatsCalculator import StatsCalculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = StatsCalculator()

    def test_calculator_instantiate(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_addition(self):
        test_data = CsvReader(TestFiles.ADDITION_FILE_NAME).data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_calculator_division(self):
        test_data = CsvReader(TestFiles.DIVISION_FILE_NAME).data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_calculator_multiplication(self):
        test_data = CsvReader(TestFiles.MULTIPLICATION_FILE_NAME).data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_calculator_square(self):
        test_data = CsvReader(TestFiles.SQUARE_FILE_NAME).data
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_calculator_square_root(self):
        test_data = CsvReader(TestFiles.SQUARE_ROOT_FILE_NAME).data
        for row in test_data:
            self.assertEqual(self.calculator.sqrt(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_calculator_subtraction(self):
        test_data = CsvReader(TestFiles.SUBTRACTION_FILE_NAME).data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    # ------------------------------------------------------------------------------------------------------------------

    def test_stats_calculator_mean_divide_by_zero(self):
        test_arr = []  # empty array will give divide by zero error
        with self.assertRaises(ZeroDivisionError):
            self.calculator.mean(test_arr)

    def test_stats_calculator_mean_str(self):
        test_arr = [1, 2, "three"]  # bad (string) input
        with self.assertRaises(ValueError):
            self.calculator.mean(test_arr)

    def test_stats_calculator_mean(self):
        test_arr = [1, 2, 3, 4, 5, 6]
        expected_value = 3.5
        self.assertEqual(self.calculator.mean(test_arr), expected_value)

    def test_stats_calculator_median(self):
        test_arr = [1, 2, 3, 4, 5]
        expected_value = 3
        self.assertEqual(self.calculator.median(test_arr), expected_value)

    def test_stats_calculator_mode(self):
        test_arr = [2, 2, 3, 1, 2, 1, 4]
        expected_value = 2
        self.assertEqual(self.calculator.mode(test_arr), expected_value)

    def test_stats_calculator_variance(self):
        test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_value = 7.5
        self.assertEqual(self.calculator.variance(test_arr), expected_value)

    def test_stats_calculator_std_dev(self):
        test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_value = 2.6457513110645907
        self.assertEqual(self.calculator.std_dev(test_arr), expected_value)


if __name__ == '__main__':
    unittest.main()
