#!/usr/bin/env python3

# test_add.py
import unittest
from add import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        try:
            self.assertEqual(add(2, 1), 4)
            print("Test 'test_add_positive_numbers' succeeded.")
        except AssertionError:
            print("Test 'test_add_positive_numbers' failed.")

    def test_add_negative_numbers(self):
        try:
            self.assertEqual(add(-2, -3), -5)
            print("Test 'test_add_negative_numbers' succeeded.")
        except AssertionError:
            print("Test 'test_add_negative_numbers' failed.")

    def test_add_mixed_numbers(self):
        try:
            self.assertEqual(add(5, -3), 2)
            print("Test 'test_add_mixed_numbers' succeeded.")
        except AssertionError:
            print("Test 'test_add_mixed_numbers' failed.")

if __name__ == "__main__":
    unittest.main()
