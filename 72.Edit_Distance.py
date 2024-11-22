class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        '''l1 = len(word1)
        l2 = len(word2)

        dp = [[-1] * (l2 + 1) for _ in range(l1 + 1)]

        for i in range(l1 + 1):
            for j in range(l2 + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        
        return dp[l1][l2]'''
        if len(word1) < len(word2):
            word1, word2 = word2, word1  # Ensure word1 is the longer word
        
        l1, l2 = len(word1), len(word2)
        prev = list(range(l2 + 1))  # Initialize the "previous" row
        
        for i in range(1, l1 + 1):
            current = [i] * (l2 + 1)  # Start a new "current" row
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    current[j] = prev[j - 1]
                else:
                    current[j] = min(prev[j], current[j - 1], prev[j - 1]) + 1
            prev = current  # Move to the next row
        
        return prev[l2]
