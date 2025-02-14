class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        n = len(nums)-1
        while i < n+1:
            mid  = i + (n - i) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid+1
            else:
                n = mid-1
        return -1 

# Time Complexity is O(n)
