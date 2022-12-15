import unittest
import day_15

class TestMethods(unittest.TestCase):

    def test_1(self):
        test_data = day_15.read_text_file("15_test.txt")
        #test_data = day_15.parse_data(test_data)
        total = day_15.part_1(test_data, 10)
        self.assertEqual(total, 26)


if __name__ == '__main__':

    unittest.main()