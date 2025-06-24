from collections import defaultdict
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # x ^ 0 = x and x ^ x = 0
                
        ans = len(nums)
        for i in range(ans):
            ans ^= i ^ nums[i]
        return ans


        # O(n) time complexity O(n) space complexity
        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1
        # temp = len(nums) + 1
        # for i in range(temp):
        #     if count[i] == 0:
        #         return i
        # Sum Method
        # return expected_sum(sum from 0 to n) - actual_sum(sum(nums))