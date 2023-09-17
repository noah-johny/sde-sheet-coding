class Solution:
    def perfectSum(self, arr, n, sum):
        dp = [[0]*(sum+1) for _ in range(n+1)]

        dp[0] = [1] + [0]*sum

        mod = 10**9 + 7

        for i in range(1, n+1):
            for j in range(sum+1):
                if arr[i-1] <= j:
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j-arr[i-1]]) % mod
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][sum]


# Driver Code
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, sum = input().split()
        n, sum = int(n), int(sum)
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.perfectSum(arr, n, sum)
        print(ans)
