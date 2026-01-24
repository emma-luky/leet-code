# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num1 = 0
        linkedlist = l1
        power = 0
        while linkedlist:
            tens = 10**power
            num1 += linkedlist.val * tens
            power += 1
            linkedlist = linkedlist.next
        
        num2 = 0
        linkedlist = l2
        power = 0
        while linkedlist:
            tens = 10**power
            num2 += linkedlist.val * tens
            power += 1
            linkedlist = linkedlist.next

        total = list(str(num1 + num2))
        head = ListNode(int(total[-1]))
        current = head
        for i in range(len(total) - 2, -1, -1):
            current.next = ListNode(int(total[i]))
            current = current.next
        return head
