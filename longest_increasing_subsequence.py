from bisect import bisect_left


class Solution:
    def longestSubsequence(self, a, n):
        longest = [a[0]]

        for i in range(1, n):
            if a[i] > longest[-1]:
                longest.append(a[i])
            else:
                index = bisect_left(longest, a[i])
                longest[index] = a[i]

        return len(longest)


# Driver Code
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.longestSubsequence(a, n))
