class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        isFound = False
        for i in range(len(matrix)):
            for j in range (len(matrix[i])):
                if target == matrix[i][j]:
                    isFound = True
                    return isFound      
                else:
                    isFound = False
        return isFound
        
        