import unittest
import day_6


class TestMethods(unittest.TestCase):

    def test_1(self):
        test_data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
        score = day_6.part_1(test_data)
        self.assertEqual(score, 5)

    def test_2(self):
        test_data = "nppdvjthqldpwncqszvftbrmjlhg"
        score = day_6.part_1(test_data)
        self.assertEqual(score, 6)

    def test_3(self):
        test_data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
        score = day_6.part_1(test_data)
        self.assertEqual(score, 10)

    def test_4(self):
        test_data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
        score = day_6.part_1(test_data)
        self.assertEqual(score, 11)

    def test_2_1(self):
        test_data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
        score = day_6.part_2(test_data)
        self.assertEqual(score, 19)

    def test_2_2(self):
        test_data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
        score = day_6.part_2(test_data)
        self.assertEqual(score, 23)

    def test_2_3(self):
        test_data = "nppdvjthqldpwncqszvftbrmjlhg"
        score = day_6.part_2(test_data)
        self.assertEqual(score, 23)

    def test_2_4(self):
        test_data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
        score = day_6.part_2(test_data)
        self.assertEqual(score, 29)

    def test_2_5(self):
        test_data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
        score = day_6.part_2(test_data)
        self.assertEqual(score, 26)


if __name__ == '__main__':


    unittest.main()