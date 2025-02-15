class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l = 1
        r = max(piles)
        #sort(piles)
        def caneatAll(speed):
            total_hrs = sum((pile+speed-1)//speed for pile in piles)
            return total_hrs <=h
        
        while l < r:
            mid = (l+r)//2
            if caneatAll(mid):
                r = mid
            else:
                l = mid + 1
        
        return l

# Time complexity is O(mlog(n)) where m is len(piles) and n is max(piles)



        
