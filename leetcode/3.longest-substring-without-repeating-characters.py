#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, 0  
        max_len = 0
        char_set = set()  

        while j < len(s):
            if s[j] not in char_set:
                char_set.add(s[j])
                max_len = max(max_len, j - i + 1)
                j += 1 
            else:
                char_set.remove(s[i])
                i += 1  

        return max_len
# Time complexity is O(n)
        
# @lc code=end

