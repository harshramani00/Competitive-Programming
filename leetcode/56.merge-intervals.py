#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
                continue
            start = res[-1][0]
            end = res[-1][1]
            if intervals[i][0] > end:
                res.append(intervals[i])
            else:
                res[-1] = [
                    min(intervals[i][0],start),
                    max(intervals[i][1],end)
                ]
        return res
            
        

# Time Complexity: O(nlogn) for sorting the intervals and O(n) for merging them 
# @lc code=end

