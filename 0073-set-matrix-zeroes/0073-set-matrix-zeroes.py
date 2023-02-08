class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = collections.defaultdict(set)
        c = collections.defaultdict(set)
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    r[i].add(i)
                    c[j].add(j)
                    
        for i in range(rows):
            for j in range(cols):        
                if (i in r) or (j in c):
                    matrix[i][j] = 0
                
                # if (j in c):
                #     matrix[i][j] = 0
                    
        