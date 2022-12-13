# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        sumListHead = l1
        currentL1 = l1
        currentL2 = l2
        rest = 0

        while(True):
            l1Val = currentL1.val
            
            l2Val = 0
            if currentL2 != None:
                l2Val = currentL2.val 
                currentL2 = currentL2.next

            sum = l1Val + l2Val + rest
            currentL1.val = sum % 10
            rest = sum // 10

            if currentL1.next == None and currentL2 == None and rest == 0:
                return sumListHead

            if currentL1.next == None:
                currentL1.next = ListNode()
            currentL1 = currentL1.next
