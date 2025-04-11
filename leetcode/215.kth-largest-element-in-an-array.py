#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums_max = [-i for i in nums]
        heapq.heapify(nums_max)
        for i in range(1,k):
            heapq.heappop(nums_max)
        res = -heapq.heappop(nums_max)
        return res
    
# time complexity: O(n + klogn) n is the length of nums, k is the kth largest element becase sorting in heap takes O(logn)
# space complexity: O(n) for the heap

        
# @lc code=end

