import unittest

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElementDict1(self, num):
        threshold = len(num)/2
        # print "threshold = %d" % threshold
        counts = {}
        for i in num:
            n_occur = 1
            if i in counts:
                n_occur = counts[i]+1
            if n_occur > threshold:
                return i
            counts[i] = n_occur
            # print "counts of %d's = %d" % (i, counts[i])
        # print "Shouldn't get here! No majority found"
        return None

    def majorityElementDict2(self, num):
        threshold = len(num)/2
        counts = {}
        for i in num:
            n_occur = 1
            if i in counts:
                n_occur = counts[i]+1
            if n_occur > threshold:
                return i
            counts[i] = n_occur
        return None

    majorityElementDict = majorityElementDict1

class TestSolution(unittest.TestCase):
    def test_number_of_the_feast(self):
        l = [6,6,5,5,5]
        a = 5
        self.assertEqual(a, Solution().majorityElementDict(l))
 
    def test_one_two_one_two(self):
        l = [1,2,1,2,1,2,1]
        a = 1
        self.assertEqual(a, Solution().majorityElementDict(l))
 
if __name__ == '__main__':
    unittest.main()
