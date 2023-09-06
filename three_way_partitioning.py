from collections import Counter


class Solution:
    def threeWayPartition(self, array, a, b):
        part1 = []
        part2 = []
        part3 = []
        whole = []

        for i in array:
            if (i < a):
                part1.append(i)
            elif (a <= i <= b):
                part2.append(i)
            else:
                part3.append(i)

        whole = part1+part2+part3

        for i in range(len(array)):
            array[i] = whole[i]

        return 1


# Driver Code
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        array = list(map(int, input().strip().split()))
        original = Counter(array)
        a, b = list(map(int, input().strip().split()))
        ob = Solution()
        ob.threeWayPartition(array, a, b)

        k1 = k2 = k3 = 0
        for e in array:
            if e > a:
                k3 += 1
            elif e <= a and e >= b:
                k2 += 1
            elif e < a:
                k1 += 1

        m1 = m2 = m3 = 0
        for e in range(k1):
            if array[e] < a:
                m1 += 1
        for e in range(k1, k1+k2):
            if array[e] <= a and array[e] >= b:
                m2 += 1
        for e in range(k1+k2, k1+k2+k3):
            if array[e] >= a:
                m3 += 1

        flag = False
        if k1 == m1 and k2 == m2 and k3 == m3:
            flag = True
        for e in range(len(array)):
            original[array[e]] -= 1
        for e in range(len(array)):
            if original[array[e]] != 0:
                flag = False
        if flag:
            print(1)
        else:
            print(0)
