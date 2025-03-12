#
# @lc app=leetcode id=572 lang=python
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def isSameTree(p, q):

            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return (isSameTree(p.left,q.left) and isSameTree(p.right,q.right))


        def findAndCheck(p, q):
            if not p:
                return False
            if p.val == q.val and isSameTree(p, q):
                return True
            return findAndCheck(p.left, q) or findAndCheck(p.right, q)

        return findAndCheck(root, subRoot)
#time complexity: O(n*m) where n is the number of nodes in the root tree and m is the number of nodes in the subtree
        
# @lc code=end

