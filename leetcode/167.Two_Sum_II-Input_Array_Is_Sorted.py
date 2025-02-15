class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while r > l:
            if numbers[r] + numbers[l] == target:
                return [l + 1, r + 1]
            elif numbers[r] + numbers[l] > target:
                r -= 1
            else:
                l += 1
        return [-1, -1]
