class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sumDigit = 0
        x_list = list(str(x))
        for i in x_list:
            sumDigit += int(i)
        
        if x % sumDigit == 0:
            return sumDigit
        else:
            return -1


        