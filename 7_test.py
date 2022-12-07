import unittest
import day_7

class TestMethods(unittest.TestCase):

    def test_1(self):
        test_data = day_7.read_text_file("7_test.txt")
        total = day_7.part_1(test_data)

        self.assertEqual(total, 95437)


if __name__ == '__main__':

    unittest.main()