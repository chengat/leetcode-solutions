class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = str(x[::-1])
        print(x, y)
        if x == y:
            return True
        else: 
            return False





        