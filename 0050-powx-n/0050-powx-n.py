class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        n + -
        n odd even
        
        """
        if n == 0:
            return 1

        def pwer(x,n):
            if n == 1:
              return x
            a = b = self.myPow(x,n//2)
            
            if n % 2:
                b *= x
            return a * b
        
        ans = pwer(x,abs(n))
        if n < 0:
            return 1 / ans
        
        return ans

        