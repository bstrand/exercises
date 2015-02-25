# https://oj.leetcode.com/problems/implement-strstr/

import unittest

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle, depth=0):
        # print "{} in {} ? d={}".format(needle,haystack,depth)
        if not len(needle):
            return 0
        if not len(haystack):
            return -1
        if len(haystack) < len(needle):
            return -1
        if haystack[:len(needle)] == needle:
            return depth
        else:
            return self.strStr(haystack[1:], needle, depth+1)


    def strStrSlowWithHelperMethod(self, haystack, needle):
        for i in range(len(haystack)):
            if self.starts_with(haystack[i:], needle):
                return i
        if len(haystack) == 0:
            if len(needle) == 0:
                return 0
        return -1

    def starts_with(self, full, prefix):
        f_len = len(full)
        p_len = len(prefix)
        if f_len < p_len:
            return False
        # print "Full: {}, Prefix: {}".format(full, prefix)
        for i in range(p_len):
            if full[i] != prefix[i]:
                return False
        return True

    def strStrBrute(self, haystack, needle):
        h_len = len(haystack)
        n_len = len(needle)
        if not n_len:
            return 0
        if h_len < n_len:
            return -1

        # print "Full: {} ({}), Prefix: {} ({})".format(haystack, h_len, needle, n_len)
        for i in range(h_len):
            for j in range(n_len):
                # print "h[{}]:n[{}] {}:{}".format(i+j, j, haystack[i+j], needle[j])                
                if i + n_len > h_len :
                    return -1 
                if haystack[i+j] == needle[j]:
                    if j == n_len-1:
                        return i
                    next
                else:
                    break
        return -1

class TestSolution(unittest.TestCase):
    def test_01(self):
        sln = Solution()
        haystack = 'abcffoob'
        needle = 'foo'
        self.assertEqual(haystack.find(needle), sln.strStr(haystack, needle))

    def test_mississippi(self):
        sln = Solution()
        haystack = 'mississippi'
        needle = 'issipi'
        self.assertEqual(haystack.find(needle), sln.strStr(haystack, needle))

    def test_aaa(self):
        sln = Solution()
        haystack = 'aaa'
        needle = 'aaaa'
        self.assertEqual(haystack.find(needle), sln.strStr(haystack, needle))

    def test_a_empty(self):
        sln = Solution()
        haystack = 'a'
        needle = ''
        self.assertEqual(haystack.find(needle), sln.strStr(haystack, needle))

    def test_empty_a(self):
        sln = Solution()
        haystack = ''
        needle = 'a'
        self.assertEqual(haystack.find(needle), sln.strStr(haystack, needle))

    def test_a_a(self):
        sln = Solution()
        haystack = 'a'
        needle = 'a'
        self.assertEqual(haystack.find(needle), sln.strStr(haystack, needle))

    def test_empty_empty(self):
        sln = Solution()
        haystack = ''
        needle = ''
        self.assertEqual(haystack.find(needle), sln.strStr(haystack, needle))

if __name__ == '__main__':
    unittest.main()
