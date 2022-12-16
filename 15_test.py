import unittest
import day_15

class TestMethods(unittest.TestCase):

    # def test_1(self):
    #     test_data = day_15.read_text_file("15_test.txt")
    #     #test_data = day_15.parse_data(test_data)
    #     total = day_15.part_1(test_data, 10)
    #     self.assertEqual(total, 26)

    # def test_2(self):
    #     test_data = day_15.read_text_file("15_test.txt")
    #     #test_data = day_15.parse_data(test_data)
    #     total = day_15.part_2(test_data, 20)
    #     self.assertEqual(total, 56000011)

    # def test_3(self):
    #     test_data = day_15.read_text_file("15_test.txt")
    #     #test_data = day_15.parse_data(test_data)
    #     total = day_15.part_2_fast(test_data, 20)
    #     self.assertEqual(total, 56000011)

    def test_4(self):
        test_data = day_15.read_text_file("15_test.txt")
        #test_data = day_15.parse_data(test_data)
        total = day_15.part_2_morefast(test_data, 20)
        self.assertEqual(total, 56000011)

if __name__ == '__main__':

    unittest.main()