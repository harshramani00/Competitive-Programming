class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #return min(nums)
        l = 0
        r = len(nums) - 1
        #min = 0
        while l <= r:
            if nums[l] > nums[r]:
                l += 1
            if nums[r] > nums[l]:
                r -= 1
            if l == r:
                return nums[l]


# Time complexity is O(n)
