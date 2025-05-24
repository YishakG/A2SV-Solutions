class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ops = 0

        while len(nums) >= 2 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            new_val = 2 * x + y
            heapq.heappush(nums, new_val)
            ops += 1

        return ops if all(num >= k for num in nums) else -1