class Solution:
    def removeDuplicates(self, str):
        no_duplicate_list = []

        for character in str:
            if character not in no_duplicate_list:
                no_duplicate_list.append(character)

        return ("".join(no_duplicate_list))


# Driver Code
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        str = input().strip()
        ob = Solution()
        ans = ob.removeDuplicates(str)
        print(ans)
        tc -= 1
