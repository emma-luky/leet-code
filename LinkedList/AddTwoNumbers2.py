# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        def number(list: Optional[ListNode]) -> int:
            count = 0
            curr = list
            num = 0
            while (curr):
                num += curr.val * (10**count)
                count += 1
                curr = curr.next
            return num

        sum = number(l1) + number(l2)
        start = ListNode()
        curr = start
        while (sum > 0):
            digit = sum % 10
            sum //= 10
            curr.val = digit
            if sum == 0:
                break
            curr.next = ListNode()
            curr = curr.next
        return start

