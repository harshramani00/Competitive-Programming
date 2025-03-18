#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        res = set()
        subset = []

        nums.sort()

        def dfs(start):
            if start == len(nums):
                res.add(tuple(subset))
                return


            subset.append(nums[start])
            dfs(start+1)

            subset.pop()
            dfs(start + 1)
        dfs(0)
        return [list(s) for s in res]
    

# time: O(2^n)        
# @lc code=end

