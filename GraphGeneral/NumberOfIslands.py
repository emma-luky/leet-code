class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            q = deque()
            visited.add((row, col))
            q.append((row, col))
            while q:
                curr_row, curr_col = q.popleft()
                checks = [[1,0], [-1,0], [0,1], [0, -1]]
                for dr, dc in checks:
                    row, col = curr_row + dr, curr_col + dc
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == '1' and (row, col) not in visited:
                        q.append((row, col))
                        visited.add((row, col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    islands += 1
                    bfs(row, col)
        return islands
