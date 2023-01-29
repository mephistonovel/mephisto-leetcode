class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        matrix2 = matrix[:]
        for i in range(length):
            matrix[i] = [matrix2[j][i] for j in range(length-1,-1,-1)]
        
        ### solution ###
#         class Solution:
#             def rotate(self, matrix: List[List[int]]) -> None:
#                 self.transpose(matrix)
#                 self.reflect(matrix)

#             def transpose(self, matrix):
#                 n = len(matrix)
#                 for i in range(n):
#                     for j in range(i + 1, n):
#                         matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] #python이라 가능한 swapping

#             def reflect(self, matrix):
#                 n = len(matrix)
#                 for i in range(n):
#                     for j in range(n // 2):
#                         matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j] #