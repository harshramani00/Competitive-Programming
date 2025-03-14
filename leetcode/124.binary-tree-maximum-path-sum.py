#
# @lc app=leetcode id=124 lang=python
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            

            maxsumleft = max(dfs(root.left),0)
            maxsumright = max(dfs(root.right),0)

            res[0] = max(res[0],root.val + maxsumleft+ maxsumright)
            return root.val +max(maxsumleft,maxsumright)

        dfs(root)
        return res[0]
    
#time complexity: O(N) because we visit each node once
#space complexity: O(H) where H is the height of the tree
        
# @lc code=end

