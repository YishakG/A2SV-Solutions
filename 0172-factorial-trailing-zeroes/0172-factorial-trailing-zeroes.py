class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Time Complexity: O(log(n)) base 5 Space Complexity: O(log(n)) base 5
        if n < 5:
            return 0
        return n//5 + self.trailingZeroes(n//5)