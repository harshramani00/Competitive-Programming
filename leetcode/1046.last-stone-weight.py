#
# @lc app=leetcode id=1046 lang=python
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            x = max(stones)
            stones.remove(x)
            y = max(stones)
            stones.remove(y)
            if x == y:
                continue
            else:
                stones.append(x-y)
        return stones[0] if len(stones) == 1 else 0
    
# time complexity: O(n^2)
# space complexity: O(1)
 

        
# @lc code=end

