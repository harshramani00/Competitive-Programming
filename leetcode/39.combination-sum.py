#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        subset = []
        def dfs(i,total):
            if i == len(candidates):
                return
            if target < total:
                return
            if target == total:
                res.append(list(subset))
                return
            for j in range(i, len(candidates)):
                subset.append(candidates[j])
                dfs(j, total + candidates[j]) 
                subset.pop()

        dfs(0,0)
        return res
#time complexity: O(2^n)
        
# @lc code=end

