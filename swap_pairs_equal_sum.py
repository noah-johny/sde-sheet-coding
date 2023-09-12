class Solution:
    def findSwapValues(self, a, n, b, m):
        if n < 1 or m < 1:
            return -1

        sum_a = sum(a)
        sum_b = sum(b)
        b = set(b)

        diff = sum_a - sum_b

        if diff % 2 != 0:
            return -1

        diff = diff // 2

        for num in a:
            if num - diff in b:
                return 1

        return -1


# Driver Code
if __name__ == '__main__':

    t = int(input())
    for _ in range(0, t):
        l = list(map(int, input().split()))
        n = l[0]
        m = l[1]
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a, n, b, m))
