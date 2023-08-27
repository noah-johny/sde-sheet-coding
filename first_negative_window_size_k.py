def printFirstNegativeInteger(A, N, K):

    result = []
    queue = []

    for i in range(N):

        while queue and queue[0] < i - K + 1:
            queue.pop(0)

        if A[i] < 0:
            queue.append(i)

        if i >= K - 1:
            result.append(A[queue[0]] if queue else 0)

    return result


# Driver Code
def main():

    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())

        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()
