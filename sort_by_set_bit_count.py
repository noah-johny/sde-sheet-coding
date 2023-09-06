class Solution:
    def sortBySetBitCount(self, arr, n):
        return arr.sort(key=lambda x: bin(x).replace("0b", "").count("1"), reverse=True)


# Driver Code
def main():

    T = int(input())

    while (T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortBySetBitCount(arr, n)
        print(*arr)

        T -= 1


if __name__ == "__main__":
    main()
