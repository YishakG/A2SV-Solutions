class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        ans = []
        def backtrack(start):
            if len(path) == k:
                ans.append(path[:])
                return 
            for candidate in range(start+1,n+1):
                path.append(candidate)
                backtrack(candidate)
                path.pop()
        backtrack(0)
        return ans