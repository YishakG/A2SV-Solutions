class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Time Complexity: O(log(n)) Space Complexity: O(log(n)) base 4 but doesnt matter
        if n == 1:
            return True
        if 0 <= n < 1:
            return False
        return self.isPowerOfFour(n/4)
        