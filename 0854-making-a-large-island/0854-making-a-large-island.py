class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2
        island_sizes = {}
        def dfs(x, y, island_id):
            if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] != 1:
                return 0
            grid[x][y] = island_id
            size = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                size += dfs(x + dx, y + dy, island_id)
            return size
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i, j, island_id)
                    island_sizes[island_id] = size
                    island_id += 1

        max_island = max(island_sizes.values(), default=0)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    size = 1   
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n:
                            id = grid[ni][nj]
                            if id > 1 and id not in seen:
                                seen.add(id)
                                size += island_sizes[id]
                    max_island = max(max_island, size)
        return max_island if max_island > 0 else n * n
