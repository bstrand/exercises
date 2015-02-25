# https://oj.leetcode.com/problems/valid-parentheses/

import unittest

class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1:
            return "1"

        i = 1
        for x in range(n-1):
            i = self.say_num_of(i)
        return str(i)

    def say_num_of(self, n):

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
        result = int("".join(accum))
        # print "%d -> %d" % (n, result)
        return result

def countAndSayConcise(self, n):
    res = '1'
    for i in range(n-1):
        stack = []
        for (k, g) in itertools.groupby(res):
            stack.append(str(len(list(g)))+k)
        res = ''.join(stack)
    return res

class TestSolution(unittest.TestCase):
    def test_01(self):
        sln = Solution()
        self.assertEqual("1", sln.countAndSay(1))

    def test_02(self):
        sln = Solution()
        self.assertEqual("11", sln.countAndSay(2))
 
    def test_03(self):
        sln = Solution()
        self.assertEqual("21", sln.countAndSay(3))
 
    def test_04(self):
        sln = Solution()
        self.assertEqual("1211", sln.countAndSay(4))
 
    def test_05(self):
        sln = Solution()
        self.assertEqual("111221", sln.countAndSay(5))
 
    def test_06(self):
        sln = Solution()
        self.assertEqual("312211", sln.countAndSay(6))
 
    def test_07(self):
        sln = Solution()
        self.assertEqual("13112221", sln.countAndSay(7))
 
if __name__ == '__main__':
    unittest.main()
