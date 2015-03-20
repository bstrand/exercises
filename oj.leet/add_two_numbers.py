# https://oj.leetcode.com/problems/add-two-numbers/

import unittest
from linked_list import ListNode
from linked_list import LinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
      p1 = l1.head
      p2 = l2.head
      acc = ListNode()
      current = None
      while p1 or p2:
        n1 = p1.val if p1 else 0
        n2 = p2.val if p2 else 0
        p1 = p1.next
        p2 = p2.next

        new_node = ListNode(n1+n2)
        if not acc.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
      return acc


class TestSolution(unittest.TestCase):

    def test_1_2(self):
        sln = Solution()
        self.assertEqual(str(LinkedList(from_list=[3])), str(sln.addTwoNumbers(LinkedList(from_list=[1]),LinkedList(from_list=[2]))))

    def test_30_11(self):
        sln = Solution()
        self.assertEqual(str(LinkedList(from_list=[1,4])), str(sln.addTwoNumbers(LinkedList(from_list=[0,3]),LinkedList(from_list=[1,1]))))

    def test_1_0(self):
        sln = Solution()
        self.assertEqual(str(LinkedList(from_list=[1])), str(sln.addTwoNumbers(LinkedList(from_list=[1]),LinkedList(from_list=[0]))))

    def test_0_1(self):
        sln = Solution()
        self.assertEqual(str(LinkedList(from_list=[1])), str(sln.addTwoNumbers(LinkedList(from_list=[0]),LinkedList(from_list=[1]))))

if __name__ == '__main__':
    unittest.main()
