class Solution:
    def isFascinating(self, n: int) -> bool:
        newString = str(n) + str(2*n) + str(3*n)
        #print(newString)
        stringSet = set(newString)
        #print(stringSet)
        containsZero = False
        if '0' in stringSet:
            containsZero = True
        
        if (len(newString) == len(stringSet)) and (containsZero == False):
            return True
        else:
            return False
        