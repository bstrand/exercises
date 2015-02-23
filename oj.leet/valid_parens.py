# https://oj.leetcode.com/problems/valid-parentheses/

import unittest

class Solution:
    # @return a boolean
    openers = {'{':'}','[':']', '(':')'}
    closers = {v: k for k, v in openers.items()}
    
    def isValid(self, s):
        next_close = []
        for c in s:
            #print "c: %c" % c
            if c in self.openers.keys():
                next_close.append(self.openers[c])
            elif c in self.closers.keys():
                if not next_close or next_close.pop() != c:
                    #print "INVALID"
                    return False
        #print "next_close len = %d --> %r" % (len(next_close), len(next_close) == 0)
        return not next_close

class TestSolution(unittest.TestCase):
    def test_one_of_each(self):
        sln = Solution()
        self.assertEqual(True, sln.isValid("{}()[]"))
 
    def test_one_of_each_nested(self):
        sln = Solution()
        self.assertEqual(True, sln.isValid("{([])}"))
 
    def test_two_interleaved(self):
        sln = Solution()
        self.assertEqual(False, sln.isValid("([)]"))
 
    def test_two_left_open(self):
        sln = Solution()
        self.assertEqual(False, sln.isValid("(["))
 
    def test_two_close_only(self):
        sln = Solution()
        self.assertEqual(False, sln.isValid("])"))
 
if __name__ == '__main__':
    unittest.main()
