class Solution:
    def rearrange(self, arr, n):
        positive = []
        negative = []
        positive_len = negative_len = 0

        for i in arr:
            if i >= 0:
                positive.append(i)
            else:
                negative.append(i)

        arr.clear()
        positive_len = len(positive)
        negative_len = len(negative)

        for i in range(0, min(positive_len, negative_len)):
            arr.append(positive[i])
            arr.append(negative[i])

        if positive_len > negative_len:
            arr.extend(positive[negative_len:])
        elif positive_len < negative_len:
            arr.extend(negative[positive_len:])


# Driver Code
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
