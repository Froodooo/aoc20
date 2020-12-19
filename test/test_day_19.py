import unittest

import day19.day_19


class TestDay19(unittest.TestCase):
    def test_run_a_example_1(self):
        output = day19.day_19.run_a('test/19_example_1.txt')
        self.assertEqual(output, 2)

    def test_run_a_example_2(self):
        output = day19.day_19.run_a('test/19_example_2.txt')
        self.assertEqual(output, 2)

    def test_run_a_example_3(self):
        output = day19.day_19.run_a('test/19_example_3.txt')
        self.assertEqual(output, 3)

    def test_run_b_example_3(self):
        output = day19.day_19.run_b('test/19_example_3.txt')
        self.assertEqual(output, 12)


if __name__ == '__main__':
    unittest.main()
