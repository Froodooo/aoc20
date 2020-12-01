import unittest
import sys

sys.path.append("day1")
from day_1 import Day1

class TestDay1(unittest.TestCase):
    def setUp(self):
        self.day1 = Day1()

    def test_run_a(self):
        output = self.day1.run_a('day1/1_example_1.txt')
        self.assertEqual(output, 514579)

    def test_run_b(self):
        output = self.day1.run_b('day1/1_example_1.txt')
        self.assertEqual(output, 241861950)

if __name__ == '__main__': 
    unittest.main()