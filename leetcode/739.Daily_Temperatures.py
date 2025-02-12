class Solution(object):
    def dailyTemperatures(self, temp):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temp)
        ans = [0] * n  
        high = 0 
        count = 0  

        i = n - 1  
        while i >= 0:
            if i == n - 1:  
                ans[i] = 0  
                high = temp[i]
                count = 0  
            
            elif temp[i] >= high:  
                high = temp[i]
                ans[i] = 0
                count = 0  
            else:  
                count = 1 
                while i + count < n and temp[i + count] <= temp[i]:  
                    if ans[i + count] == 0:  
                        count = 0
                        break
                    count += ans[i + count]  

                ans[i] = count  

            i -= 1  

        return ans
