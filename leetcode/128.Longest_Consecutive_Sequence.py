class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        nums = sorted(set(nums))
        longest = 1
        seq = 1
        
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                seq += 1
            else:
                longest = max(longest, seq)
                seq = 1 
        
        return max(longest, seq)
# time complexity is O(nlog(n))
