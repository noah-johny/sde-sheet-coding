class Solution:
    def maxSumPairWithDifferenceLessThanK(self, arr, N, K):
        arr.sort()
        dp = [0] * N
        dp[0] = 0
        pairSum = 0

        for i in range(1, N):
            dp[i] = dp[i-1]

            if (arr[i] - arr[i-1] < K):
                pairSum = arr[i] + arr[i-1]

                if (i == 1):
                    dp[i] = max(dp[i], pairSum)
                else:
                    dp[i] = max(dp[i], dp[i-2] + pairSum)

        return dp[N-1]


# Driver Code
def main():

    T = int(input())

    while (T > 0):
        N = int(input())
        arr = [int(x) for x in input().strip().split()]
        K = int(input())
        ob = Solution()
        print(ob.maxSumPairWithDifferenceLessThanK(arr, N, K))

        T -= 1


if __name__ == "__main__":
    main()
