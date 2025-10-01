class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        isBulky = isHeavy = False
        volume = length * width * height
        category = ""
        if length >= 10**4 or width >= 10**4 or height >= 10**4 or volume >= 10**9:
            isBulky = True
        if mass >= 100:
            isHeavy = True

        if isHeavy == True and isBulky == False:
            category = "Heavy"
        if isHeavy == False and isBulky == True:
            category = "Bulky"
        elif isHeavy == True and isBulky == True:
            category = "Both"
        elif isHeavy == False and isBulky == False:
            category = "Neither"
        
        return category