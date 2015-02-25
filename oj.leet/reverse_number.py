import unittest

class Solution:
    # @return an integer
    def reverse(self, x):
        debug = False

        if debug:
          print "x: %d" % x

        sign = 1
        if x < 0:
          sign = -1
          x = 0 - x

        rx = 0
        while x:
          rx = rx * 10 + x % 10
          x = x / 10
          if debug:
            print "x: {0: >6}\t rx: {1: >6}\t rem = {2}".format(x,rx,x%10)

        if debug:
          print "rx: %d" % rx * sign

        # Special case for silly fake overflow
        if 2147483648 < rx:
          return 0

        return rx * sign

class TestSolution(unittest.TestCase):

    def test_1234(self):
        sln = Solution()
        self.assertEqual(4321, sln.reverse(1234))

    def test_1(self):
        sln = Solution()
        self.assertEqual(1, sln.reverse(1))

    def test_0(self):
        sln = Solution()
        self.assertEqual(0, sln.reverse(0))

    def test_100021(self):
        sln = Solution()
        self.assertEqual(120001, sln.reverse(100021))

    def test_neg12(self):
        sln = Solution()
        self.assertEqual(-21, sln.reverse(-12))

    def test_overflow(self):
        sln = Solution()
        #self.assertEqual(9646324351, sln.reverse(1534236469))
        self.assertEqual(0, sln.reverse(1534236469))

if __name__ == '__main__':
    unittest.main()
