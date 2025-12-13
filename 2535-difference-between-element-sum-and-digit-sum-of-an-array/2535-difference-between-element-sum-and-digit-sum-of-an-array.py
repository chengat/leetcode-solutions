class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum, digitSum = sum(nums), 0
        strNums = ""
        for i in nums:
            strNums += str(i)
        for j in strNums:
            digitSum += int(j)
        return abs(digitSum - elementSum)
        
        
        