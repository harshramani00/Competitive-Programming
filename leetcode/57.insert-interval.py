#
# @lc app=leetcode id=57 lang=python
#
# [57] Insert Interval
#

# @lc code=start
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        inserted = False

        for interval in intervals:
            if newInterval[1] < interval[0]:
                if not inserted:
                    res.append(newInterval)
                    inserted = True
                res.append(interval)
            elif interval[1] < newInterval[0]:
                res.append(interval)
            else:
                newInterval = [
                    min(interval[0],newInterval[0]),
                    max(interval[1],newInterval[1])
                ]
        
        if not inserted:
            res.append(newInterval)

        return res
        
# @lc code=end

