import unittest
from odd_even import check_odd_even


class TestOddEven(unittest.TestCase):

    def test_even(self):
        self.assertEqual(check_odd_even(2), "Even")

    def test_odd(self):
        self.assertEqual(check_odd_even(7), "Odd")

    def test_zero(self):
        self.assertEqual(check_odd_even(0), "Even")

    def test_negative_even(self):
        self.assertEqual(check_odd_even(-4), "Even")

    def test_negative_odd(self):
        self.assertEqual(check_odd_even(-3), "Odd")

    def test_invalid_string(self):
        with self.assertRaises(ValueError):
            check_odd_even("abc")

    def test_float(self):
        with self.assertRaises(ValueError):
            check_odd_even(2.5)

    def test_boolean(self):
        with self.assertRaises(ValueError):
            check_odd_even(True)


if __name__ == "__main__":
    unittest.main()