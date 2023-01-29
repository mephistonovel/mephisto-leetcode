class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        matrix2 = matrix[:]
        for i in range(length):
            matrix[i] = [matrix2[j][i] for j in range(length-1,-1,-1)]