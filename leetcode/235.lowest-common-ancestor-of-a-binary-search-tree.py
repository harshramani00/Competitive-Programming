#
# @lc app=leetcode id=235 lang=python
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None 
        
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root 

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q) 

        return self.lowestCommonAncestor(root.left, p, q)
    
#time complexity: O(n) where n is the number of nodes in the tree
        
# @lc code=end

