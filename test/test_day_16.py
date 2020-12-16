import unittest

import day16.day_16


class TestDay16(unittest.TestCase):
    def test_run_a_example_1(self):
        output = day16.day_16.run_a('test/16_example_1.txt')
        self.assertEqual(output, 71)

    def test_run_b_example_2(self):
        output = day16.day_16.run_b('test/16_example_2.txt')
        self.assertEqual(output, 0)


if __name__ == '__main__':
    unittest.main()
