import sys


class Solution:
    def count(self, coins, N, Sum):
        dp = [0] * (sum + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, sum + 1):
                dp[i] += dp[i - coin]

        return dp[sum]


# Driver Code
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        sum, N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins, N, sum))
