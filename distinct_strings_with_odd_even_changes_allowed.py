def encodeString(string):
    odd = [0]*26
    even = [0]*26

    for i in range(len(string)):
        index = ord(string[i]) - ord('a')

        if i & 1:
            odd[index] += 1
        else:
            even[index] += 1

    encoded = ""

    for i in range(26):
        encoded += str(even[i]) + "-" + str(odd[i]) + "-"

    return encoded


def countDistinct(input, n):
    distinct = set()
    count = 0

    for string in input:
        encoded = encodeString(string)

        if encoded not in distinct:
            distinct.add(encoded)
            count += 1

    return count


# Driver Code
if __name__ == "__main__":
    input = ["abcd", "acbd", "adcb", "cdba", "bcda", "badc"]
    n = len(input)
    print(countDistinct(input, n))
