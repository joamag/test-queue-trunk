#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from main import sum_two_numbers


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_two_numbers(2, 3), 6)
        self.assertEqual(sum_two_numbers(0, 0), 0)
        self.assertEqual(sum_two_numbers(-1, 1), 0)


if __name__ == "__main__":
    unittest.main()
