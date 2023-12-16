import unittest
import day_14

class TestMethods(unittest.TestCase):

    def test_1(self):
        test_data = day_14.read_text_file("14_test.txt")
        max_row, max_column = day_14.get_max(test_data)
        test_data = day_14.parse_data(test_data, max_row, max_column)
        total = day_14.part_1(test_data, max_row, max_column)
        self.assertEqual(total, 24)

    def test_2(self):
        test_data = day_14.read_text_file("14_test.txt")
        max_row, max_column = day_14.get_max(test_data)
        column_bunce = max_row*2
        max_column+=column_bunce
        test_data = day_14.parse_data(test_data, max_row, max_column)
        total = day_14.part_2(test_data, max_row, max_column)
        self.assertEqual(total, 93)

if __name__ == '__main__':

    unittest.main()