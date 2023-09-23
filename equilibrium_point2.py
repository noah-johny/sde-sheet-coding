import math


class Solution:
    def equilibriumPoint(self, A, N):
        if N < 1 or N == 2:
            return -1
        elif N == 1:
            return 1

        left, right = 1, N-2
        sum_left, sum_right = A[0], A[-1]

        while left <= right:
            if left == right and sum_left == sum_right:
                return left+1

            if sum_left < sum_right:
                sum_left += A[left]
                left += 1
            else:
                sum_right += A[right]
                right -= 1

        return -1


# Driver Code
def main():
    T = int(input())

    while (T > 0):
        N = int(input())
        A = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.equilibriumPoint(A, N))
        T -= 1


if __name__ == "__main__":
    main()
