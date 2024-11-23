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
        num1, num2 = 0,0

        while l1 or l2:
            if l1:
                num1 = num1 * 10 + l1.val
                l1 = l1.next
            if l2:
                num2 = num2 * 10 + l2.val
                l2 = l2.next
        
        num1 += num2

        dummy = ListNode(0)  
        current = dummy

        if num1 == 0:
            return ListNode(0)

        for digit in str(num1):
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next
        

        
