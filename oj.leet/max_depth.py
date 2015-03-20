import unittest

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
		
		if root == None:
			return 0
		
		if not root.left and not root.right:
			return 1
		else:
			return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class TestSolution(unittest.TestCase):
	def test_t1(self):
		t1 = TreeNode(1)
		t1.left = TreeNode(2)
		t1.left.left = TreeNode(3)
		sln = Solution()
		self.assertEqual(3, sln.maxDepth(t1))

if __name__ == '__main__':
    unittest.main()