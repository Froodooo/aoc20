import unittest

from day7.day_7 import Day7


class TestDay7(unittest.TestCase):
    def setUp(self):
        self.day = Day7()

    def test_run_a_example_1(self):
        output = self.day.run_a('test/7_example_1.txt')
        self.assertEqual(output, 4)
    
    def test_run_b_example_1(self):
        output = self.day.run_b('test/7_example_1.txt')
        self.assertEqual(output, 32)

    def test_run_b_example_2(self):
        output = self.day.run_b('test/7_example_2.txt')
        self.assertEqual(output, 126)


if __name__ == '__main__':
    unittest.main()
