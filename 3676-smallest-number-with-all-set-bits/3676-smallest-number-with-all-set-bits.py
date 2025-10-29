class Solution:
    def smallestNumber(self, n: int) -> int:
        count = 0
        while n >= 1:
            count += 1
            n /= 2
        return 2**count - 1
        
            