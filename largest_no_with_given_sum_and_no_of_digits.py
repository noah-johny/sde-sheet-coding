class Solution:
    def findLargest(self, N, S):
        res = ""
        digits = 0

        if S == 0 and N > 1:
            return -1

        while S >= 0:
            if S < 10:
                res += str(S)
                res += "0" * (N-len(res))
                return res
            else:
                res += "9"
                digits += 1

                if digits == N:
                    return -1
            S -= 9


# Driver Code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]

        ob = Solution()
        print(ob.findLargest(N, S))
