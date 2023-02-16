class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols= len(board), len(board[0])
        q = deque()
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    if i==0 or i == rows-1 or j==0 or j==cols-1:
                        board[i][j]='C'
                        q.append((i,j))
        
        # finq = deque()
        # print(q[0])        
      # 특정 ,i,j에 대해 시행할 bfs즉, 가장자리의 것! 
        def bfs(q):
            # visited = set()
            while q:
                i,j = q.popleft()
                for row,col in [[i,j-1],[i-1,j],[i,j+1],[i+1,j]]:
                    if 0<row<rows and 0<col<cols and board[row][col] == 'O':
                        board[row][col]='C'
                        q.append((row,col))

        for orow,ocol in q:
            tmpq = deque()
            tmpq.append((orow,ocol))
            bfs(tmpq)
            
            
        # print(board)
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='C':
                    board[i][j]='O'
                    
        
        ### https://leetcode.com/problems/surrounded-regions/discuss/3135985/Easy-to-understand-PYTHON-solution-beats-93-with-proper-comments ### 
#         rows, cols= len(board), len(board[0])

#         def capture(r,c): 
#             if (r<0 or r==rows or c<0 or c==cols or board[r][c]!="O"):
#                 return 
#             board[r][c]="T"
#             capture(r+1,c)
#             capture(r-1,c)
#             capture(r,c+1)
#             capture(r,c-1)

#         #(DFS)capture unsurrounded region(0->T)
#         for r in range(rows):
#             for c in range(cols):
#                 if board[r][c]=="O" and (r==0 or r==rows-1 or c==0 or c==cols-1):
#                     capture(r,c)

#         #capture surrounded region(0->x)
#         for r in range(1,rows-1):
#             for c in range(1,cols-1):
#                 if board[r][c]=="O":
#                     board[r][c]="X" 

#         #uncapture unsurrounded region(T->0)
#         for r in range(rows):
#             for c in range(cols):
#                 if board[r][c]=="T":
#                     board[r][c]="O" 
