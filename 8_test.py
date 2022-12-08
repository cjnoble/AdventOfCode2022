import unittest
import day_8

class TestMethods(unittest.TestCase):

    def test_1(self):
        test_data = day_8.read_text_file("8_test.txt")
        total = day_8.part_1(test_data)
        self.assertEqual(total, 21)

    def test_2(self):
        test_data = day_8.read_text_file("8.txt")
        total = day_8.part_1(test_data)
        self.assertEqual(total, 1843)

    def test_3(self):
        test_data = day_8.read_text_file("8_test.txt")
        total = day_8.part_2(test_data)
        self.assertEqual(total, 8)

if __name__ == '__main__':

    unittest.main()