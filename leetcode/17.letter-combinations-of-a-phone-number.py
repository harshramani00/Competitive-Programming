#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if digits == "":
            return []
        res = []
        digitToChar ={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        def backtrack(i,string):
            if len(string) == len(digits):
                res.append(string)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, string + c)

        backtrack(0,"")

        return res
        
# @lc code=end

