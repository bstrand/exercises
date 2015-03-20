minimum_depth.py

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
      if not root:
        return 0
      return self.minDepthRecurse(root, 1)

    def minDepthRecurse(self, root, depth):
      if not root.left and not root.right:
        return depth

      l_depth = depth
      r_depth = depth
      if root.left:
        l_depth = self.minDepthRecurse(root.left, depth+1)
      if root.right:
        r_depth = self.minDepthRecurse(root.right, depth+1)

      return min(l_depth,r_depth)
        
class TestSolution(unittest.TestCase):

    def test_one_three(self):
        sln = Solution()
        # self.assertEqual(3, sln.singleNumber([1,1,2,2,3,4,4]))

    def test_two_zeros(self):
        sln = Solution()
        # self.assertEqual(4, sln.singleNumber([3,3,0,1,1,0,4]))