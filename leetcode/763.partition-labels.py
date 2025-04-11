#
# @lc app=leetcode id=763 lang=python
#
# [763] Partition Labels
#

# @lc code=start
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        lastindex = {}
        for i in range(len(s)):
            lastindex[s[i]] = i

        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1 
            end = max(end, lastindex[c])

            if i == end:
                res.append(size)
                size = 0
        return res
        
# time complexity: O(n)
# space complexity: O(1)
        
# @lc code=end

