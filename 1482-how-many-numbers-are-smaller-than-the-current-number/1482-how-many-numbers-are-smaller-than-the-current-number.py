class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        
        for i in range(len(nums)):
            count = 0
            for j in nums:
                if nums[i] > j:
                    count += 1
            ans[i] = count
        return ans
        