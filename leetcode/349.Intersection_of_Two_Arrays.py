class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2):
            return self.intersection(nums2, nums1)
        ans = []
        for i in nums1:
            if i in nums2 and i not in ans:

                ans.append(i)
        return ans
        
