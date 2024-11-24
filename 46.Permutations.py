class Solution(object):

    def fact(self, num):
        if num == 0 or num == 1:
            return 1
        return num * self.fact(num - 1)

    def swap(self, nums, i):
        nums[0], nums[i] = nums[i], nums[0]
        return nums

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def generate_permutations(nums, iteration, path):
            if iteration == 0:
                ans.append(path)
                return
            for i in range(len(nums)):
                temp = self.swap(nums[:], i)
                generate_permutations(temp[1:], iteration - 1, path + [temp[0]])

        ans = []
        iterations = self.fact(len(nums))
        generate_permutations(nums, len(nums), [])
        return ans
