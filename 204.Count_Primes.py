class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''if n <= 2:
            return 0  
        
        def is_prime(num):
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        count = 0
        for i in range(2, n):  
            if is_prime(i):
                count += 1
        
        return count'''
        if n <= 2:
            return 0
        
        # Create a boolean array to mark non-prime numbers
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
        
        # Use Sieve of Eratosthenes
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        
        # Count the number of primes
        return sum(is_prime)
         
