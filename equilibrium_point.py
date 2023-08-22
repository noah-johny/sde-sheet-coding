class Solution:
    def equilibriumPoint(self, A, N):
        if N < 3:
            return -1

        left_sum, right_sum = A[0], sum(A[2:])
        right = 2

        while right < N:
            left_sum += A[right-1]
            right_sum -= A[right]

            if left_sum == right_sum:
                return right+1

            right += 1

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
