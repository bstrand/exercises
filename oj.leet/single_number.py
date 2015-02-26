import unittest

# https://oj.leetcode.com/problems/single-number/
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        return reduce(lambda i,n: i^n, A, 0)

    def singleNumberUsingForLoop(self, A):
        i = 0
        for n in A:
            i ^= n
        return i

class TestSolution(unittest.TestCase):

    def test_one_three(self):
        sln = Solution()
        self.assertEqual(3, sln.singleNumber([1,1,2,2,3,4,4]))

    def test_two_zeros(self):
        sln = Solution()
        self.assertEqual(4, sln.singleNumber([3,3,0,1,1,0,4]))

    def test_one_zero(self):
        sln = Solution()
        self.assertEqual(0, sln.singleNumber([3,3,0,1,1,4,4]))

    def test_neg_one(self):
        sln = Solution()
        self.assertEqual(-1, sln.singleNumber([3,3,-1,1,1,4,4]))

if __name__ == '__main__':
    unittest.main()
