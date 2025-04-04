class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        
        mid = 2 ** (n - 1)
        
        if k == mid:
            return "1"
        
        if k < mid:
            return self.findKthBit(n - 1, k)
        else:
            mirrored_index = 2 ** n - k
            result = self.findKthBit(n - 1, mirrored_index)
            return "1" if result == "0" else "0"
