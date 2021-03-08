import unittest
import fizzbuzz as fb

class Testcase(unittest.TestCase):
    if (__name__ == '__main__'):
        unittest.main()

    def test_None(self):
        self.assertEqual(fb.fizzbuzz(1), 1)
        self.assertEqual(fb.fizzbuzz(11), 11)
        self.assertEqual(fb.fizzbuzz(13), 13)

    def test_fizzes(self):
        self.assertEqual(fb.fizzbuzz(3), "Fizz")
        self.assertEqual(fb.fizzbuzz(6), "Fizz")
        self.assertEqual(fb.fizzbuzz(9), "Fizz")

    def test_Buzzes(self):
        self.assertEqual(fb.fizzbuzz(5), "Buzz")
        self.assertEqual(fb.fizzbuzz(10), "Buzz")
        self.assertEqual(fb.fizzbuzz(20), "Buzz")

    def test_Fizzbuzzes(self):
        self.assertEqual(fb.fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fb.fizzbuzz(30), "FizzBuzz")
        self.assertEqual(fb.fizzbuzz(45), "FizzBuzz")
