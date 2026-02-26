class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(len(matrix[1])):
                if j > 0:
                    if matrix[i-1][j-1] == matrix[i][j]:
                        continue
                    else:
                        return False
        return True
