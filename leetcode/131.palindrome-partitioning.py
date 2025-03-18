#
# @lc app=leetcode id=131 lang=python
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res, part = [], []

        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    res.append(list(part))
                return
            
            if self.isPali(s, j, i):
                part.append(s[j : i + 1])
                dfs(i + 1, i + 1)
                part.pop()
            
            dfs(j, i + 1)
        
        dfs(0, 0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
        
# @lc code=end

