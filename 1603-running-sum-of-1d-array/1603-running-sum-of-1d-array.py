class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]] * len(nums)
        for i in range(len(nums)):
            sum = 0
            for j in range(i+1):
                sum += nums[j]
            ans[i] = sum
        return ans

