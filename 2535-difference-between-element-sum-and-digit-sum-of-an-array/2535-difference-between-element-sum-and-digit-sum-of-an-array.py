class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum, digitSum = 0, 0
        strNums = ""
        for i in nums:
            elementSum += i
            strNums += str(i)
        for j in strNums:
            digitSum += int(j)
        return abs(digitSum - elementSum)
        
        
        