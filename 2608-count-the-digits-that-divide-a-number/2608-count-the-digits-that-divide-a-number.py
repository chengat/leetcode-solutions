class Solution:
    def countDigits(self, num: int) -> int:
        strNum = str(num)
        count = 0
        for i in range(len(strNum)):
            if num % int(strNum[i]) == 0:
                count += 1
        return count

        