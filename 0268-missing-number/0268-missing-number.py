from collections import defaultdict
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        temp = len(nums) + 1
        for i in range(temp):
            if count[i] == 0:
                return i