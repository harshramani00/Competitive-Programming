#
# @lc app=leetcode id=239 lang=python
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        l = 0
        r = k - 1 
        ans = []

        while r < len(nums):
            window = nums[l:r+1]  
            ans.append(max(window)) 
            l += 1
            r += 1  

        return ans
# time complexity is O(nk)

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        ans = []
        window = deque()

        for i in range(len(nums)):
            if window and window[0] < i - k + 1:
                window.popleft()

            while window and nums[window[-1]] < nums[i]:
                window.pop()

            window.append(i)

            if i >= k - 1:
                ans.append(nums[window[0]])

        return ans
# time complexity is O(n)
        
# @lc code=end

