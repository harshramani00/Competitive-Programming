class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == len(set(nums)):
            return False
        else: return True
        
# Time Complexity is O(n) Due ti set()
