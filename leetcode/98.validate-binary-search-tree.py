#
# @lc app=leetcode id=98 lang=python
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False
            return validate(node.left, lower, node.val) and validate(node.right, node.val, upper)
        
        return validate(root)
#time complexity: O(n) where n is the number of nodes in the tree
        
# @lc code=end

