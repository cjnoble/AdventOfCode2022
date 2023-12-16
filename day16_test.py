import unittest
import day_16

class TestMethods(unittest.TestCase):

    def test_1(self):
        test_data = day_16.read_text_file("16_test.txt")
        #test_data = day_16.parse_data(test_data)
        total = day_16.part_1(test_data, day_16.TIME)
        self.assertEqual(total, 1651)


if __name__ == '__main__':

    unittest.main()