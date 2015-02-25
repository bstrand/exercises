# https://oj.leetcode.com/problems/valid-parentheses/

import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

class LList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, new_node):
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def len(self):
        count = 0;
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __repr__(self):
        current = self.head
        nodes = []
        while current:
            nodes.append("{}".format(current))
            current = current.next
        return " -> ".join(nodes)

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        long_head = headA
        short_head = headB
        long_len = self.list_len(headA)
        short_len = self.list_len(headB)
        if long_len < short_len: # nope, reverse it
            temp = long_head
            temp_len = long_len
            long_head = short_head
            long_len = short_len
            short_head = temp
            short_len = temp_len
        long_start_offset = long_len - short_len
        print "Offset = %d" % long_start_offset

        short_node = short_head
        long_node = long_head
        for x in range(long_start_offset):
            #print "Skipping {}".format(long_node)
            long_node = long_node.next

        for x in range(short_len):
            #print "Comparing {} - {}".format(long_node, short_node)
            if short_node == long_node:
                return short_node
            short_node = short_node.next
            long_node = long_node.next

        return None

    def list_len(self, list_head):
        count = 0;
        current = list_head
        while current:
            count += 1
            current = current.next
        return count


class TestSolution(unittest.TestCase):
    def test_prob_example(self):
        sln = Solution()
        
        la = LList()
        la.insert(ListNode('a1'))
        la.insert(ListNode('a2'))

        lb = LList()
        lb.insert(ListNode('b1'))
        lb.insert(ListNode('b2'))
        lb.insert(ListNode('b3'))

        c1 = ListNode('c1')
        lc = LList()
        lc.insert(c1)
        lc.insert(ListNode('c2'))
        lc.insert(ListNode('c3'))

        la.insert(c1)
        lb.insert(c1)

        # print la
        # print lb
        # print lc

        sln = Solution()
        self.assertEqual('c1', sln.getIntersectionNode(la.head, lb.head).val)
 
    def test_a_longer(self):
        sln = Solution()
        
        la = LList()
        la.insert(ListNode('a1'))
        la.insert(ListNode('a2'))
        la.insert(ListNode('a3'))

        lb = LList()
        lb.insert(ListNode('b1'))
        lb.insert(ListNode('b2'))

        c1 = ListNode('c1')
        lc = LList()
        lc.insert(c1)
        lc.insert(ListNode('c2'))
        lc.insert(ListNode('c3'))

        la.insert(c1)
        lb.insert(c1)

        sln = Solution()
        self.assertEqual('c1', sln.getIntersectionNode(la.head, lb.head).val)
 
    def test_same_len(self):
        sln = Solution()
        
        la = LList()
        la.insert(ListNode('a1'))
        la.insert(ListNode('a2'))

        lb = LList()
        lb.insert(ListNode('b1'))
        lb.insert(ListNode('b2'))

        c1 = ListNode('c1')
        lc = LList()
        lc.insert(c1)
        lc.insert(ListNode('c2'))

        la.insert(c1)
        lb.insert(c1)

        sln = Solution()
        self.assertEqual('c1', sln.getIntersectionNode(la.head, lb.head).val)
 
    def test_only_one_list(self):
        sln = Solution()
        
        la = LList()
        lb = LList()

        c1 = ListNode('c1')
        lc = LList()
        lc.insert(c1)
        lc.insert(ListNode('c2'))

        la.insert(c1)
        lb.insert(c1)

        sln = Solution()
        self.assertEqual('c1', sln.getIntersectionNode(la.head, lb.head).val)
 
if __name__ == '__main__':
    unittest.main()
