import functools


class Solution:
    def printLargest(self, arr):
        def sort_key(a, b):
            if (a+b) > (b+a):
                return -1
            elif (a+b) < (b+a):
                return 1
            else:
                return 0

        ans = ""
        sorted_arr = sorted(arr, key=functools.cmp_to_key(sort_key))

        for num in sorted_arr:
            ans += num

        return ans


# Driver Code Starts
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(arr)
        print(ans)
        tc -= 1
