#
# @lc app=leetcode id=567 lang=python
#
# [567] Permutation in String
#

# @lc code=start
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count_s1 = {}
        for i in range(len(s1)):
            count_s1[s1[i]] = count_s1.get(s1[i],0)+1
        l , r = 0, 0

        count_window = count_s1.copy()
        while r < len(s2):
            if s2[r] not in count_s1:
                count_window = count_s1.copy()
                l = r+1
            else:
                count_window[s2[r]] = count_window.get(s2[r],0)-1
                while count_window[s2[r]] < 0:
                    count_window[s2[l]] += 1
                    l += 1
                if r-l+1 == len(s1):
                    return True
            r += 1
        return False
# Time Complexity is O(n)
        
# @lc code=end

