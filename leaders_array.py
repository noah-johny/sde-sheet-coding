class Solution:
    def leaders(self, A, N):
        leaders = []
        leaders.append(A[N-1])
        maxValue = A[N-1]

        for i in range(N-2, -1, -1):
            if A[i] >= maxValue:
                leaders.append(A[i])
                maxValue = A[i]

        leaders.reverse()
        return leaders


# Driver Code
def main():

    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        obj = Solution()

        A = obj.leaders(A, N)

        for i in A:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()
