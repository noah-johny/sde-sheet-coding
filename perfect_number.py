class Solution:
    def isPerfectNumber(self, N):
        if N <= 1:
            return 0

        perfect_sum = 1

        for i in range(2, int(N ** 0.5) + 1):
            if N % i == 0:
                perfect_sum += i

                if i != N // i:
                    perfect_sum += N // i

        if perfect_sum == N:
            return 1
        else:
            return 0


# Driver Code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.isPerfectNumber(N))
