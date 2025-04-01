class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def distance(point):
            x, y = point
            return math.sqrt(x**2 + y**2)
        dist_tuples = [(distance(i),i) for i in points]
        dist_tuples.sort()
        res = [coord for _, coord in dist_tuples[:k]]
        return res
    
# Time Complexity: O(nlogn) where n is the number of points. The sorting step dominates the time complexity - log(n).
# Space Complexity: O(n) for storing the distance tuples.