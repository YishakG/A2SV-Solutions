class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 1
             
            if grid[i][j] == -1:
                return 0
            
             
            grid[i][j] = -1
            
            perimeter = 0
             
            perimeter += dfs(i - 1, j)  # Up
            perimeter += dfs(i + 1, j)  # Down
            perimeter += dfs(i, j - 1)  # Left
            perimeter += dfs(i, j + 1)  # Right
            
            return perimeter
        
         
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:  
                    return dfs(i, j)
        
        return 0  
