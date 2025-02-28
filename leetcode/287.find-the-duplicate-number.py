#
# @lc app=leetcode id=287 lang=python
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictt = {}
        for i in nums:
            if i in dictt:
                dictt[i]+=1
            else:
                dictt[i]=1
        for i,j in dictt.items():
            if j>1:
                return i
            
# time complexity is O(n)
        
# @lc code=end

