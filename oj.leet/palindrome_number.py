# https://oj.leetcode.com/problems/palindrome-number/

import unittest

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
      return self.isPalindromeNumeric(x)

    def isPalindromeNumeric(self, x):
      # print "\n--------------\nx:{}\n".format(x)
      i = 0
      if(x<0 or (x % 10 == 0 and x != 0)):
        return False
      while (i < x):
        i = i * 10 + x % 10
        x = x / 10
        # print "i: {0: >6}\t\tx: {1: >6}\t\ti/10: {2: >6}".format(i, x, i/10)
      return (i == x or i/10 == x)

    def isPalindromeAsStr(self, x):
      # print "-------------------------"
      if x < 0:
        return False
      elif x / 10 == 0:
        return True
      else:
        return self.isPalindromeStrRec(str(x))

    def isPalindromeStrRec(self, x):
      #print x
      l = len(x)
      if not l or l == 1:
        return True
      if x[0] ==  x[-1]:
        return self.isPalindromeStrRec(x[1:-1])
      else:
        return False

    def isPalindromeNumericFail(self, x):
        print "-------------------------"
        if x < 0:
          return False
        if x / 10 == 0:
          return True

        pow10 = 0
        tenx = x / 10
        while tenx:
          tenx = tenx / 10
          pow10 += 1
        mag = int(pow(10,pow10))
        least = x % 10
        most = x / mag
        print "%d %d %d %d %d" % (x, pow10, mag, least, most)
        if least == most:
          new_x = (x / 10) - ((mag / 10) * (x / mag))
          print "new_x = %d" % new_x
          return self.isPalindrome(new_x)
        else:
          return False

    def isPalindromeTooEasy(self, x):
        return int(str(abs(x))[::-1]) == x


class TestSolution(unittest.TestCase):


    def test_a1000021(self):
        sln = Solution()
        self.assertEqual(False, sln.isPalindrome(1000021))

    def test_a1200021(self):
        sln = Solution()
        self.assertEqual(True, sln.isPalindrome(1202021))

    def test_121(self):
        sln = Solution()
        self.assertEqual(True, sln.isPalindrome(121))

    def test_11(self):
        sln = Solution()
        self.assertEqual(True, sln.isPalindrome(11))

    def test_1(self):
        sln = Solution()
        self.assertEqual(True, sln.isPalindrome(1))

    def test_1221(self):
        sln = Solution()
        self.assertEqual(True, sln.isPalindrome(1221))

    def test_12521(self):
        sln = Solution()
        self.assertEqual(True, sln.isPalindrome(12521))

    def test_12(self):
        sln = Solution()
        self.assertEqual(False, sln.isPalindrome(12))

    def test_115(self):
        sln = Solution()
        self.assertEqual(False, sln.isPalindrome(115))

if __name__ == '__main__':
    unittest.main()
