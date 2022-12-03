import unittest
import day_3


test_data = day_3.read_text_file("3_test.txt")


class TestMethods(unittest.TestCase):

    def test_1(self):

        score = day_3.part_1(test_data)

        self.assertEqual(score, 157)



if __name__ == '__main__':
    unittest.main()

