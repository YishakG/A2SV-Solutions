class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # decreasing monotonic stack
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1][1] - i
            stack.append([temperatures[i],i])
        return ans