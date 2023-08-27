class Solution:
    def longestCommonPrefix(self, arr, n):
        arr.sort()

        prefix = arr[0]
        prefix_len = len(arr[0])

        for i in arr:
            while (i[0: prefix_len] != prefix):
                prefix_len -= 1
                prefix = prefix[0: prefix_len]

        return prefix if prefix_len > 0 else -1


# Driver Code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr, n))
