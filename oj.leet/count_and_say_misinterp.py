# https://oj.leetcode.com/problems/valid-parentheses/

import unittest

class Solution:
    # @return a string
    def countAndSay(self, n):
        accum = []
        prev = None
        seq_count = 0
        for i in str(n):
            if not prev:
                seq_count = 1
                prev = i
            elif i == prev:
                seq_count += 1
            else:
                accum.append("%d%s" % (seq_count, prev))                
                seq_count = 1
                prev = i
        accum.append("%d%s" % (seq_count, prev))                
        result = "".join(accum)
        print "%s -> %s\n----------\n" % (n, result)
        return result

class TestSolution(unittest.TestCase):
    def test_one_one(self):
        sln = Solution()
        self.assertEqual("11", sln.countAndSay(1))
 
    def test_two_ones(self):
        sln = Solution()
        self.assertEqual("21", sln.countAndSay(11))
 
    def test_one_two_one_one(self):
        sln = Solution()
        self.assertEqual("1211", sln.countAndSay(21))
 
    def test_one_two_three(self):
        sln = Solution()
        self.assertEqual("111213", sln.countAndSay(123))
 
    def test_z_long_one(self):
        sln = Solution()
        self.assertEqual("215336", sln.countAndSay(1133333666))
 
if __name__ == '__main__':
    unittest.main()
