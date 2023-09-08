class Solution:
    def maxFrequency(self, freq):
        maxCount = 0
        maxChar = ""
        for key, value in freq.items():
            if value > maxCount:
                maxCount = value
                maxChar = key

        return maxCount, maxChar

    def rearrangeString(self, str):
        freq = {}
        char = []

        for ch in str:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
                char.append(ch)

        size = len(str)

        maxCount, maxChar = self.maxFrequency(freq)

        if maxCount > (size+1) // 2:
            return "-1"

        result = [""] * size
        index = 0

        char.remove(maxChar)

        while maxCount:
            result[index] += maxChar
            maxCount -= 1
            index += 2

        for ch in char:
            while freq[ch] > 0:
                if index >= size:
                    index = 1

                result[index] += ch
                freq[ch] -= 1
                index += 2

        return "".join(result)


# Driver Code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str1 = input()
        solObj = Solution()
        str2 = solObj.rearrangeString(str1)
        if str2 == '-1':
            print(0)
        elif sorted(str1) != sorted(str2):
            print(0)
        else:
            for i in range(len(str2)-1):
                if str2[i] == str2[i+1]:
                    print(0)
                    break
            else:
                print(1)
