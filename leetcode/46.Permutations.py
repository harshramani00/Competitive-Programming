class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        permutes = self.permute(nums[1:])

        res = []

        for p in permutes:
            for i in range (len(p) + 1):
                p_copy = list(p)
                p_copy.insert(i,nums[0])
                res.append(p_copy)
        return res

        
            
            
                       