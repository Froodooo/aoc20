import unittest

import day11.day_11_dirty


class TestDay10(unittest.TestCase):
    def test_run_a_example_1(self):
        output = day11.day_11_dirty.run_a('test/11_example_1.txt')
        self.assertEqual(output, 37)
    
    def test_run_b_example_1(self):
        output = day11.day_11_dirty.run_b('test/11_example_1.txt')
        self.assertEqual(output, 26)


if __name__ == '__main__':
    unittest.main()
