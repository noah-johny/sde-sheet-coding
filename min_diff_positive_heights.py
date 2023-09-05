class Solution:
    def getMinDiff(self, arr, n, k):
        if n <= 1:
            return 0
        
        arr.sort()
        
        diff = max(arr) - min(arr)
        
        for i in range(1, n):
            if arr[i]-k >= 0:
                min_val = min(arr[i]-k, arr[0]+k)
                max_val = max(arr[i-1]+k, arr[-1]-k)
                diff = min(max_val - min_val, diff)
            
        return diff

# Driver Code
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1