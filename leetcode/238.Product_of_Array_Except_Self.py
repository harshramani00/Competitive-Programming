class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        ans = [1] * length  # Initialize the answer array with 1's
        
        # Calculate the prefix products
        prefix = 1
        for i in range(length):
            ans[i] = prefix
            prefix *= nums[i]
        
        # Calculate the suffix products and multiply with the prefix products
        suffix = 1
        for i in range(length - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        
        return ans
