class Solution:
    i = 2

    def isLucky(self, n):
        if self.i > n:
            return 1

        if n % self.i == 0:
            return 0

        next_pos = n - (n // self.i)
        self.i += 1

        return self.isLucky(next_pos)


# Driver Code
if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        n = int(input())
        obj = Solution()
        if obj.isLucky(n):
            print(1)
        else:
            print(0)
