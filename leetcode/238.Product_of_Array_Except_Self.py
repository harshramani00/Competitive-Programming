# Time Complexity is O(n)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        ans = [1] * length
        
        
        prefix = 1
        for i in range(length):
            ans[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(length - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        
        return ans
