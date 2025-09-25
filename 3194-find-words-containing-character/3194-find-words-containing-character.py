class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        output = []
        for i in words:
            for y in range(len(words)):
                if x in words[y]:
                    output.append(y)
            break    
                    
        return output

        