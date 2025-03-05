class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = left = right = 0
        for char in s:
            if char == "R":
                right += 1
            else:
                left += 1
            if left == right:
                left = right = 0
                count += 1
        return count