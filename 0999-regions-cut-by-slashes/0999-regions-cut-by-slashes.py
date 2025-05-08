class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.parent[y_root] = x_root

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        dsu = DSU(4 * n * n)
        for i in range(n):
            for j in range(n):
                cell_base = 4 * (i * n + j)
                char = grid[i][j]
                if char == ' ':
                    dsu.union(cell_base + 0, cell_base + 1)
                    dsu.union(cell_base + 1, cell_base + 2)
                    dsu.union(cell_base + 2, cell_base + 3)
                elif char == '/':
                    dsu.union(cell_base + 0, cell_base + 3)
                    dsu.union(cell_base + 1, cell_base + 2)
                elif char == '\\':
                    dsu.union(cell_base + 0, cell_base + 1)
                    dsu.union(cell_base + 2, cell_base + 3)
                if i > 0:
                    neighbor_base = 4 * ((i-1) * n + j)
                    dsu.union(cell_base + 0, neighbor_base + 2)
             
                if j > 0:
                    neighbor_base = 4 * (i * n + (j-1))
                    dsu.union(cell_base + 3, neighbor_base + 1)
        
        
        roots = set()
        for i in range(4 * n * n):
            roots.add(dsu.find(i))
        return len(roots)