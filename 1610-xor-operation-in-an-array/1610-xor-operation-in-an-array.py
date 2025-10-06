class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [0] * n
        output = 0

        for i in range(n):
            nums[i] = start + 2 * i 
            output ^= nums[i]
        
        return output
           


         