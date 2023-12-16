import unittest
import day_18

class TestMethods(unittest.TestCase):

    def test_1(self):
        test_data = [[1,1,1], [2,1,1]]
        #test_data = day_18.parse_data(test_data)
        total = day_18.part_1(test_data)
        self.assertEqual(total, 10)

    def test_1p2(self):
        test_data = [[1,1,1], [2,1,1]]
        #test_data = day_18.parse_data(test_data)
        total = day_18.part_2(test_data)
        self.assertEqual(total, 10)

    def test_2(self):
        test_data = day_18.read_text_file("18_test.txt")
        #test_data = day_18.parse_data(test_data)
        total = day_18.part_1(test_data)
        self.assertEqual(total, 64)

    def test_p2(self):
        test_data = day_18.read_text_file("18_test.txt")
        #test_data = day_18.parse_data(test_data)
        total = day_18.part_2(test_data)
        self.assertEqual(total, 58)

if __name__ == '__main__':

    unittest.main()