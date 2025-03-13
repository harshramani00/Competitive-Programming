#
# @lc app=leetcode id=199 lang=python
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        if not root:
            return []

        res = []

        def DFS(root, depth):
            if not root:
                return None
            if len(res) == depth:
                res.append(root.val)
            DFS(root.right, depth+1)
            DFS(root.left, depth+1)
        DFS(root, 0)
        return res

#time complexity: O(n) where n is the number of nodes in the tree

        
# @lc code=end

