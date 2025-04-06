#
# @lc app=leetcode id=252 lang=python
#
# [252] Meeting Rooms
#

# @lc code=start
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True
        intervals.sort(key = lambda x: x.start)
        prev_end = intervals[0].end
        for i in range(1,len(intervals)):
            #print(intervals[i].start)
            if intervals[i].start < prev_end:
                return False
            prev_end = intervals[i].end
        return True
    
# Time complexity: O(nlogn) for sorting the intervals 
        
# @lc code=end

