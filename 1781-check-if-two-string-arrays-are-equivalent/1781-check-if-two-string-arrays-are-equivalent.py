class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str_word1 = str_word2 = ""
       
        for i in range(len(word1)):
            str_word1 += word1[i]
        
        for j in range(len(word2)):
            str_word2 += word2[j]
           
            
        if str_word1 == str_word2:
            return True
        else:
            return False
        