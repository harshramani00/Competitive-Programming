class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1  
        mv = 0  # Max volume

        while l < r:
            mh = min(height[l], height[r])
            mv = max(mv, mh * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return mv
