#
# @lc app=leetcode id=1448 lang=python
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def count(root, maxval):
            if not root:
                return 0
            res = 1 if root.val >= maxval else 0

            maxval = max(maxval,root.val)
            res += count(root.right,maxval)
            res += count(root.left,maxval)
            return res
        return count(root,root.val)
    

#time complexity: O(n) where n is the number of nodes in the tree
        
# @lc code=end

