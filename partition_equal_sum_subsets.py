import sys


class Solution:
    def equalPartition(self, N, arr):
        if N <= 1:
            return False

        total_sum = sum(arr)

        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2

        dp = [[False] * (target_sum + 1) for _ in range(N + 1)]

        for i in range(N + 1):
            dp[i][0] = True

        for i in range(1, N + 1):
            for j in range(1, target_sum + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[N][target_sum]


# Driver Code
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])

        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
