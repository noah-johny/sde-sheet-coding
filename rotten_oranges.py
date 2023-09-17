class Solution:
    def orangesRotting(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        rotten = []
        time = 0
        fresh_count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while rotten and fresh_count > 0:
            time += 1

            new_rotten = []
            for row, col in rotten:
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        fresh_count -= 1
                        new_rotten.append((new_row, new_col))

            rotten = new_rotten

        return time if fresh_count == 0 else -1


# Driver Code
T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        a = list(map(int, input().split()))
        grid.append(a)
    obj = Solution()
    ans = obj.orangesRotting(grid)
    print(ans)
