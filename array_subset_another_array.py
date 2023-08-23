def isSubset(a1, a2, n, m):

    for value in a2:
        if value in a1:
            a1.pop(a1.index(value))
        else:
            return "No"

    return "Yes"


# Driver Code
def main():

    T = int(input())

    while (T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]

        print(isSubset(a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()
