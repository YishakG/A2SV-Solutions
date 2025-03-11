class Solution:
    def factorial(self,n):
        if n <= 1:
            return 1
        
        return n * self.factorial(n - 1)
    def trailingZeroes(self, n: int) -> int:    
        fact = self.factorial(n)
        trailing_zeros = 0
        while fact % 10 == 0:
            trailing_zeros += 1
            fact //= 10
        return trailing_zeros
         
         