#
# @lc app=leetcode id=435 lang=python
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prev_end:
                count += 1
            else:
                prev_end = end  
        
        return count
        
# Time Complexity: O(nlogn) for sorting the intervals and O(n) for iterating through them
        
# @lc code=end

