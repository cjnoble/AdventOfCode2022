import unittest
import day_11

class TestMethods(unittest.TestCase):

    def test_1(self):
        test_data = day_11.read_text_file("11_test_1.txt")
        total = day_11.part_1(test_data, 20, 3)
        self.assertEqual(total, 10605)

    def test_2(self):
        test_data = day_11.read_text_file("11_test_1.txt")
        total = day_11.part_1(test_data, 10000, 1)
        self.assertEqual(total, 2713310158)

if __name__ == '__main__':

    unittest.main()