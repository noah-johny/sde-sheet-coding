class Solution:
    def getPairsCount(self, arr, n, k):

        count = 0
        frequency = {}

        for num in arr:
            complement = k - num

            if complement in frequency:
                count += frequency[complement]

            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        return count


# Driver Code
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1
