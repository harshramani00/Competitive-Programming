#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#

# @lc code=start
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        def dfs(start, total, subset):
            if total == target:
                res.append(list(subset))
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue 
                
                if total + candidates[i] > target:
                    break 
                
                subset.append(candidates[i])
                dfs(i + 1, total + candidates[i], subset)
                subset.pop()

        dfs(0, 0, [])
        return res
    
#time complexity: O(2^n)
        
# @lc code=end

