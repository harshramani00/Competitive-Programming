class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
      #Time complexity is O(m+n)
        nums1 += nums2
      #Time complexity is O(m+n log(m+n))
        nums1.sort()
        n = len(nums1)
        mid = n//2
        if n%2 == 0: 
            return (float(nums1[mid-1])+float(nums1[mid]))/2
        else:
            return nums1[mid]
        
