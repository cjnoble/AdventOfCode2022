import unittest
import day_12

class TestMethods(unittest.TestCase):

    def test_1(self):
        test_data = day_12.read_text_file("12_test.txt")
        total = day_12.part_1(test_data)
        self.assertEqual(total, 31)

    def test_2(self):
        test_data = day_12.read_text_file("12_test.txt")
        total = day_12.part_2(test_data)
        self.assertEqual(total, 29)

if __name__ == '__main__':

    unittest.main()