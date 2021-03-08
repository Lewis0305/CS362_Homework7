import unittest
import leap_year as ly

class Testcase(unittest.TestCase):
    if (__name__ == '__main__'):
        unittest.main()

    def test_None(self):
        self.assertEqual(ly.leap_year(3), "No")
        self.assertEqual(ly.leap_year(63), "No")
        self.assertEqual(ly.leap_year(119), "No")