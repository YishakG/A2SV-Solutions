class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n, m = len(grid), len(grid[0])
        elements = []
         
        for i in range(n):
            row = sorted(grid[i], reverse=True)
           
            for j in range(min(limits[i], m)):
                elements.append(row[j])
        
         
        elements.sort(reverse=True)
        
          
        result = sum(elements[:k])
        
        return result