#
# @lc app=leetcode id=45 lang=python
#
# [45] Jump Game II
#

# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        l, r = 0, 0
        while r < len(nums) -1:
            r_margin = 0
            for i in range(l, r+1):
                r_margin = max(r_margin, i + nums[i])
            l = r + 1
            r = r_margin
            jumps += 1
        return jumps
        
# @lc code=end

