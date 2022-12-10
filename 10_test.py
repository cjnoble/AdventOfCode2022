import unittest
import day_10

class TestMethods(unittest.TestCase):

    def test_1(self):
        test_data = day_10.read_text_file("10_test_1.txt")
        total = day_10.part_1(test_data, [5])
        self.assertEqual(total, {5: 20})

    def test_2(self):
        test_data = day_10.read_text_file("10_test_2.txt")
        total = day_10.part_1(test_data, [20, 60, 100, 140, 180, 220])
        self.assertEqual(total, {20: 420, 60: 1140, 100: 1800, 140: 2940, 180: 2880, 220: 3960})


if __name__ == '__main__':

    unittest.main()