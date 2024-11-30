import unittest
from unittest.mock import patch
import pytest
from app.calc import Calculator, InvalidPermissions
import math

# Mock function to simulate permission validation
def mocked_validation(*args, **kwargs):
    return True

@pytest.mark.unit
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # Test the add method with valid inputs
    def test_add_method_returns_correct_result(self):
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertAlmostEqual(self.calc.add(2.5, 2.5), 5.0)

    # Test the subtract method with valid inputs
    def test_subtract_method_returns_correct_result(self):
        self.assertEqual(self.calc.substract(5, 3), 3)
        self.assertEqual(self.calc.substract(-2, -2), 0)
        self.assertAlmostEqual(self.calc.substract(5.5, 2.5), 3.0)

    # Test the multiply method with permission granted
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(self.calc.multiply(3, 2), 6)
        self.assertEqual(self.calc.multiply(-1, 3), -3)
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0)

    # Test the multiply method raises InvalidPermissions when permission denied
    @patch('app.util.validate_permissions', return_value=False)
    def test_multiply_method_raises_invalid_permissions(self, _validate_permissions):
        with self.assertRaises(InvalidPermissions):
            self.calc.multiply(3, 2)

    # Test the divide method with valid inputs
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    # Test divide method raises TypeError when dividing by zero
    def test_divide_method_fails_with_zero(self):
        with self.assertRaises(TypeError):
            self.calc.divide(3, 0)

    # Test the power method with valid inputs
    def test_power_method_returns_correct_result(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertAlmostEqual(self.calc.power(2.5, 2), 6.25)

    # Test square_root method with valid input
    def test_square_root_method_returns_correct_result(self):
        self.assertAlmostEqual(self.calc.square_root(4), 2.0)
        self.assertAlmostEqual(self.calc.square_root(9), 3.0)
        self.assertAlmostEqual(self.calc.square_root(2.25), 1.5)

    # Test square_root method raises ValueError for negative input
    def test_square_root_method_fails_with_negative(self):
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)

    # Test log_base_10 method with valid input
    def test_log_base_10_method_returns_correct_result(self):
        self.assertAlmostEqual(self.calc.log_base_10(100), 2.0)
        self.assertAlmostEqual(self.calc.log_base_10(10), 1.0)
        self.assertAlmostEqual(self.calc.log_base_10(1), 0.0)

    # Test log_base_10 method raises ValueError for zero or negative input
    def test_log_base_10_method_fails_with_non_positive(self):
        with self.assertRaises(ValueError):
            self.calc.log_base_10(0)
        with self.assertRaises(ValueError):
            self.calc.log_base_10(-10)

    # Test check_type method raises TypeError for non-numeric input
    def test_check_type_method(self):
        with self.assertRaises(TypeError):
            self.calc.check_type("a")
        with self.assertRaises(TypeError):
            self.calc.check_type(None)
        with self.assertRaises(TypeError):
            self.calc.check_type(object())

    # Test type checking method raises TypeError for non-numeric inputs in add method
    def test_add_method_fails_with_non_numeric(self):
        self.assertRaises(TypeError, self.calc.add, "a", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "b")

    # Test type checking method raises TypeError for non-numeric inputs in subtract method
    def test_subtract_method_fails_with_non_numeric(self):
        self.assertRaises(TypeError, self.calc.substract, "a", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "b")

    # Test type checking method raises TypeError for non-numeric inputs in multiply method
    @patch('app.util.validate_permissions', side_effect=mocked_validation)
    def test_multiply_method_fails_with_non_numeric(self, _validate_permissions):
        self.assertRaises(TypeError, self.calc.multiply, "a", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "b")

    # Test type checking method raises TypeError for non-numeric inputs in divide method
    def test_divide_method_fails_with_non_numeric(self):
        self.assertRaises(TypeError, self.calc.divide, "a", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "b")

    # Test type checking method raises TypeError for non-numeric inputs in power method
    def test_power_method_fails_with_non_numeric(self):
        self.assertRaises(TypeError, self.calc.power, "a", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "b")

    # Directly test check_types for TypeError on invalid input
    def test_check_types_method(self):
        with self.assertRaises(TypeError):
            self.calc.check_types("a", 1)
        with self.assertRaises(TypeError):
            self.calc.check_types(1, "b")
        with self.assertRaises(TypeError):
            self.calc.check_types(None, 2)
        with self.assertRaises(TypeError):
            self.calc.check_types(2, object())

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
