class Solution:
    def maximizeSum(self, a, n, k):
        maxSum = 0

        a.sort()

        for i in range(n):
            if a[i] < 0 and k > 0:
                a[i] = -(a[i])
                k -= 1

            maxSum += a[i]

        a.sort()

        if (k % 2) != 0:
            maxSum -= 2 * a[0]

        return maxSum


# Driver Code
def main():

    T = int(input())

    while (T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maximizeSum(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()
