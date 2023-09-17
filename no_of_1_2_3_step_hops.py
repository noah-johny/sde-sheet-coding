class Solution:
    def countWays(self, n):
        if n <= 2:
            return n

        mod = 1000000007
        ways = [0] * (n + 1)

        ways[0] = 1
        ways[1] = 1
        ways[2] = 2

        for step in range(3, n + 1):
            ways[step] = (ways[step - 1] + ways[step - 2] +
                          ways[step - 3]) % mod

        return ways[n]


# Driver Code
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob = Solution()
        print(ob.countWays(m))
