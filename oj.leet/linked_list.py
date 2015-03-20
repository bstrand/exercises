# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

class LinkedList:
    def __init__(self, head=None, from_list=None):
        self.head = head
        if from_list:
          [self.insert(ListNode(item)) for item in from_list]

    def __repr__(self):
        current = self.head
        nodes = []
        while current:
            nodes.append("{}".format(current))
            current = current.next
        return "[[" + " ->".join(nodes) + "->]]"

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
