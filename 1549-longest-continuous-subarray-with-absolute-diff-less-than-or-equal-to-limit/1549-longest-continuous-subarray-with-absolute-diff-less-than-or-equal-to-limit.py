class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) == 1:
            return 1
        min_que = deque()
        max_que = deque()
        l = 0
        ans = 0
        for r in range(len(nums)):
            while min_que and min_que[-1] > nums[r]:
                min_que.pop()
            min_que.append(nums[r])
            while max_que and max_que[-1] < nums[r]:
                max_que.pop()
            max_que.append(nums[r])            
            
            
            while max_que[0] - min_que[0] > limit:
                if max_que[0] == nums[l]:
                    max_que.popleft()
                if min_que[0] == nums[l]:  # Fix: Remove from min_que when needed
                    min_que.popleft()
                l += 1

            ans = max(ans,r-l+1)
        return ans
                


