class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
         
            parent = list(range(len(edges) + 1))

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])   
                return parent[x]

            def union(x, y):
                rootX = find(x)
                rootY = find(y)
                if rootX == rootY:
                    return False  
                parent[rootY] = rootX   
                return True

            for edge in edges:
                u, v = edge
                if not union(u, v):
                    return edge   

            return []
