class Solution:
    def isValid(self, word: str) -> bool:
        word = word.lower()
        #print(word)
        containsVowel = False
        containsConsonant = False
        for i in word:
            #print(i)
            if (i == "a") or (i == "e") or (i == "i") or (i == "o") or (i == "u"):
                containsVowel = True
            elif i.isalpha() == True:
                containsConsonant = True
        #print(containsVowel, containsConsonant)
       
        if (len(word) >= 3) and (word.isalnum() == True) and (containsVowel == True) and (containsConsonant == True):
            return True
        else:
            return False
        