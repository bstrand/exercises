import unittest

# https://oj.leetcode.com/problems/single-number/
class Solution:
    # @param A, a list of integer
    # @return an integer
    def max_prod_fuuuuuuu(self, rlen):
      if rlen == 0 or rlen == 1:
        return 0
      if rlen == 2:
        return 1

      max_prod = [0,0,1]
      print "rlen = %d" % rlen

      for i in range(1,rlen):
        temp_max = 0        
        for j in range(i,rlen-i):
          k = rlen - j
          print "i: {}, j: {}, k: {}".format(i,j,k)

    def max_prod(self, n):
        if n <= 1: return None
        if n == 2 or n == 3: return n - 1 # handle explicitly
        if n % 3 == 0:
            return 3 ** (n / 3)
        if n % 3 == 1:
            return 3 ** (n / 3 - 1) * 2 * 2
        else: # n % 3 == 2
            return 3 ** (n / 3) * 2

class TestSolution(unittest.TestCase):

    def test_2(self):
        sln = Solution()
        self.assertEqual(1, sln.max_prod(2))

    def test_3(self):
        sln = Solution()
        self.assertEqual(2, sln.max_prod(3))

    def test_4(self):
        sln = Solution()
        self.assertEqual(4, sln.max_prod(4))

    def test_5(self):
        sln = Solution()
        self.assertEqual(6, sln.max_prod(5))

if __name__ == '__main__':
    for n in range(2,25):
      print "%d : %d" % (n, Solution().max_prod(n))
    unittest.main()
