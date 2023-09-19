from math import log


class Solution:
    def isPowerofTwo(self, n):
        if n <= 0:
            return False
        elif n == 1:
            return True

        return 2 ** (log(n, 2) // log(2, 2)) == n


# Driver Code
def main():

    T = int(input())

    while (T > 0):

        n = int(input())
        ob = Solution()
        if ob.isPowerofTwo(n):
            print("YES")
        else:
            print("NO")

        T -= 1


if __name__ == "__main__":
    main()
