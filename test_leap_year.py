import unittest
import leap_year as ly

class Testcase(unittest.TestCase):
    if __name__ == '__main__':
        unittest.main()

    def test_None(self):
        self.assertEqual(ly.leap_year(3), "No")
        self.assertEqual(ly.leap_year(63), "No")
        self.assertEqual(ly.leap_year(119), "No")

    def test_Multi4_NonMulti100(self):
        self.assertEqual(ly.leap_year(80), "Yes")
        self.assertEqual(ly.leap_year(48), "Yes")
        self.assertEqual(ly.leap_year(8), "Yes")

    def test_Multi100_NonMulti400(self):
        self.assertEqual(ly.leap_year(200), "Yes")
        self.assertEqual(ly.leap_year(500), "Yes")
        self.assertEqual(ly.leap_year(1100), "Yes")