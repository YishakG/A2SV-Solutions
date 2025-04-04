class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        start = 0
        for i in range(2,n + 1):
            start = (start + k ) % i
        return start + 1