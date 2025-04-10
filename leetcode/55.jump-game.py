#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last = len(nums) - 1

        for i in range(len(nums) - 1, -1,-1):
            if i + nums[i] >= last:
                last = i
        return True if last == 0 else False
    
#Time complexity: O(n)
#Space complexity: O(1)
        
# @lc code=end

