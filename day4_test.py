import unittest
import day_4




class TestMethods(unittest.TestCase):

    def test_1(self):

        test_data = day_4.read_text_file("4_test.txt")
        test_data = day_4.prepare_data(test_data)

        score = day_4.part_2(test_data)

        self.assertEqual(score, 4)



if __name__ == '__main__':




    unittest.main()