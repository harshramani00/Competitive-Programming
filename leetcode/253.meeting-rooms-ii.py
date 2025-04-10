#
# @lc app=leetcode id=253 lang=python
#
# [253] Meeting Rooms II
#

# @lc code=start
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        min_heap = []
        intervals.sort(key = lambda x: x.start)
        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap,interval.end)
                
        return len(min_heap)
# Time complexity: O(nlogn)
        
# @lc code=end

