#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        
        return False
    #time complexity is O(n)
    
        
# @lc code=end

