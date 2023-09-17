class Solution:
    def printFibb(self, n):
        a, b = 1, 1

        if n < 1:
            return []
        elif n == 1:
            return [1]

        fibb = [1, 1]

        for _ in range(n-2):
            a, b = b, a+b
            fibb.append(b)

        return fibb


# Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):

        n = int(input())
        res = Solution().printFibb(n)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()