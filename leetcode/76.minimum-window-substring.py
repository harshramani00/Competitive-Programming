#
# @lc app=leetcode id=76 lang=python
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s) or len(t) == 0:
            return ""
        
        # Frequency map of characters in t
        t_count = {}
        for char in t:
            if char in t_count:
                t_count[char] += 1
            else:
                t_count[char] = 1
        
        l, r = 0, 0
        ans = ""
        window_count = {}
        matched = 0 
        
        while r < len(s):
        
            char_r = s[r]
            if char_r in window_count:
                window_count[char_r] += 1
            else:
                window_count[char_r] = 1

            if char_r in t_count and window_count[char_r] == t_count[char_r]:
                matched += 1
            
            while l <= r and matched == len(t_count):
                char_l = s[l]
                
                if ans == "" or (r - l + 1) < len(ans):
                    ans = s[l:r+1]
                
                window_count[char_l] -= 1
                if char_l in t_count and window_count[char_l] < t_count[char_l]:
                    matched -= 1
                l += 1
            r += 1
        
        return ans
#time complexity is O(n)
        
# @lc code=end

