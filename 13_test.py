import unittest
import day_13

class TestMethods(unittest.TestCase):

    def test_1(self):
        test_data = day_13.read_text_file("13_test.txt")
        total = day_13.part_1(day_13.parse_data(test_data))
        self.assertEqual(total, 13)

    def test_2(self):
        test_data = day_13.read_text_file("13_test_2.txt")
        total = day_13.part_1(day_13.parse_data(test_data))
        self.assertEqual(total, 0)

    
    def test_3(self):
        test_data = day_13.read_text_file("13_test.txt")
        total = day_13.part_2(day_13.parse_data(test_data))
        self.assertEqual(total, 140)

if __name__ == '__main__':

    unittest.main()