class Solution:
    def rearrange(self, arr, n):
        left = 0
        right = n-1

        if n > 1:
            res = arr.copy()
            arr.clear()

            while left <= right:
                if left == right:
                    arr.append(res[right])
                else:
                    arr.append(res[right])
                    arr.append(res[left])

                left += 1
                right -= 1


# Driver Code
def main():
    T = int(input())
    while (T > 0):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        ob.rearrange(arr, n)

        for i in arr:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
