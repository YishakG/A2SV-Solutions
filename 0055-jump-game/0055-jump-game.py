class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0
        for idx , num in enumerate(nums):
            if idx > end:
                return False
            end = max(end, idx + num)
        return True