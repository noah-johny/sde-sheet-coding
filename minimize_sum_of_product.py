class Solution:
    def minValue(self, a, b, n):
        a.sort(reverse=True)
        b.sort()

        min_sum = 0

        for i in range(n):
            min_sum += a[i] * b[i]

        return min_sum


# Driver Code
def main():

    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.minValue(a, b, n))

        T -= 1


if __name__ == "__main__":
    main()
