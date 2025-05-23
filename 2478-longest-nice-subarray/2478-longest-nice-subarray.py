class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        start = 0
        curr = 0   

        for end in range(n):
            while (curr & nums[end]) != 0:
                curr ^= nums[start]
                start += 1
            
            curr |= nums[end]
            max_len = max(max_len, end - start + 1)

        return max_len
