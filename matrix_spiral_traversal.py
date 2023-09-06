class Solution:
    def spirallyTraverse(self, matrix, r, c):
        size = r * c
        count = row_min = col_min = 0
        row_max = r - 1
        col_max = c - 1
        spiral = []

        while (count < size):
            for i in range(col_min, col_max+1):
                spiral.append(matrix[row_min][i])
                count += 1
                if count == size:
                    return spiral

            row_min += 1

            for i in range(row_min, row_max+1):
                spiral.append(matrix[i][col_max])
                count += 1
                if count == size:
                    return spiral

            col_max -= 1

            for i in range(col_max, col_min-1, -1):
                spiral.append(matrix[row_max][i])
                count += 1
                if count == size:
                    return spiral

            row_max -= 1

            for i in range(row_max, row_min-1, -1):
                spiral.append(matrix[i][col_min])
                count += 1
                if count == size:
                    return spiral

            col_min += 1


# Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(values[k])
                k += 1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix, r, c)
        for i in ans:
            print(i, end=" ")
        print()
