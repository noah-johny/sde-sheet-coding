class Solution:
    def findMidSum(self, ar1, ar2, n):
        if n < 1:
            return 0

        top_ar1 = top_ar2 = 0
        ar = []
        for _ in range(n*2):
            if top_ar1 == n or top_ar2 == n:
                if top_ar1 == n:
                    ar.append(ar2[top_ar2])
                    top_ar2 += 1
                else:
                    ar.append(ar1[top_ar1])
                    top_ar1 += 1
            else:
                if ar2[top_ar2] < ar1[top_ar1]:
                    ar.append(ar2[top_ar2])
                    top_ar2 += 1
                else:
                    ar.append(ar1[top_ar1])
                    top_ar1 += 1

        return ar[n-1] + ar[n]


# Driver Code
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        ar1 = list(map(int, input().strip().split()))
        ar2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMidSum(ar1, ar2, n)
        print(ans)
        tc = tc-1
