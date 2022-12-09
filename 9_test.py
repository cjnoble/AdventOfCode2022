import unittest
import day_9

class TestMethods(unittest.TestCase):

    def test_1(self):
        test_data = day_9.read_text_file("9_test.txt")
        total = day_9.part_1(test_data)
        self.assertEqual(total, 13)

    def test_2(self):
        test_data = day_9.read_text_file("9_test_2.txt")
        total = day_9.part_1(test_data)
        self.assertEqual(total, 13)

    def test_3(self):
        test_data = day_9.read_text_file("9_test.txt")
        total = day_9.part_2(test_data, 9)
        self.assertEqual(total, 1)

if __name__ == '__main__':

    unittest.main()