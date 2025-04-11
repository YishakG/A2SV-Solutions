class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        colors = [-1] * (n+1)
        graph = defaultdict(list)
        
        for u , v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(vertex,color):
            colors[vertex] = color

            for neighbour in graph[vertex]:
                if colors[neighbour] == -1:
                    if not dfs(neighbour,1 - color):
                        return False
                elif colors[neighbour] == color:
                    return False
            return True

        for i in range(1,n+1):
            if colors[i] == -1:
                if not dfs(i,0):
                    return False
        return True
                

        
        