class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)
        answer = [-1] * n
        def dfs(x):
            if answer[x] != -1:
                return answer[x]
            res = x
            for neighbor in graph[x]:
                candidate = dfs(neighbor)
                if quiet[candidate] < quiet[res]:
                    res = candidate
            
            answer[x] = res
            return res
        for i in range(n):
            dfs(i)
        
        return answer