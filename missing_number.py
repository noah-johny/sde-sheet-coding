class Solution:
    def missingNumber(self, array, n):
        array_sum = sum(array)
        req_sum = (n * (n+1)) // 2
        return req_sum - array_sum


# Driver Code
t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    s = Solution().missingNumber(a, n)
    print(s)  
