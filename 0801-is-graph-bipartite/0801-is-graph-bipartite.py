from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Colors array to mark each node:
        # -1 = unvisited/uncolored, 0 = black, 1 = white
        colors = [-1] * len(graph)
        
        def dfs(vertex, color):
            # Color the current vertex
            colors[vertex] = color

            # Visit all adjacent nodes
            for neighbour in graph[vertex]:
                if colors[neighbour] == -1:
                    # Recursively color with the opposite color
                    if not dfs(neighbour, 1 - color):
                        return False
                elif colors[neighbour] == color:
                    # If neighbor has the same color, it's not bipartite
                    return False
            return True

        # Handle disconnected components
        for i in range(len(graph)):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False
        
        return True
