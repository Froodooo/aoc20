import unittest

import day20.day_20


class TestDay20(unittest.TestCase):
    def test_run_a_example_1(self):
        output = day20.day_20.run_a('test/20_example_1.txt')
        self.assertEqual(output, 20899048083289)


if __name__ == '__main__':
    unittest.main()
