class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if row[-1] == target:
                return True
            if row[-1] < target:
                continue
            if row[-1] > target:
                for i in row:
                    if i == target:
                        return True
                    
        return False

#Worst case Time complexity is O(m+n)
#Most optimal possible is  a binary search can be used for each row, reducing row-wise search time to  O(logn)
