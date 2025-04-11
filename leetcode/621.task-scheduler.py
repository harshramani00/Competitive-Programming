#
# @lc app=leetcode id=621 lang=python
#
# [621] Task Scheduler
#

# @lc code=start
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = Counter(tasks)
        maxheap = [-i for i in count.values()]
        heapq.heapify(maxheap)

        time = 0
        q = deque()
        while maxheap or q:
            time += 1
            if maxheap:
                cnt = 1 + heapq.heappop(maxheap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time
    
# time complexity(n * m) where n is the number of tasks and m is the number of same tasks.
# space complexity O(n) for the heap and the queue
# @lc code=end

