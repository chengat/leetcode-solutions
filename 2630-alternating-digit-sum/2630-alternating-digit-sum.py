class Solution:
    def alternateDigitSum(self, n: int) -> int:
        numString = str(n)
        output = 0
        for i in range(len(numString)):
            if i % 2 == 0:
                output += int(numString[i])
            else:
                output -= int(numString[i])
        return output
        