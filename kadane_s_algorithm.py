class Solution:
    def maxSubArraySum(self, arr, N):
        maxEndingHere = maxSoFar = arr[0]

        for num in arr[1:]:
            maxEndingHere = max(num, maxEndingHere + num)
            maxSoFar = max(maxSoFar, maxEndingHere)

        return maxSoFar


# Driver Code Starts
def main():
    T = int(input())
    while (T > 0):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
