class Solution:
    def trappingWater(self, arr, n):
        left = right = water = 0

        if n in [0, 1, 2]:
            return 0

        nextHighest = max(arr[left+1:])
        for right in range(n):
            currentHeight = arr[right]
            minHeight = min(arr[left], nextHighest)

            if currentHeight < nextHighest:
                if currentHeight > arr[left]:
                    left = right
                else:
                    water += minHeight - currentHeight
            else:
                left = right
                if arr[left+1:] != []:
                    nextHighest = max(arr[left+1:])

        return water


# Driver Code
def main():
    T = int(input())
    while (T > 0):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.trappingWater(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
