class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.row_num = len(board)
        self.col_num = len(board[0])
        
        word_count = Counter(word)
        board_count = Counter(''.join([''.join(row) for row in board])) #flatten array to one string
        print(board_count)
        
        #Don't need to search if a certain character appears more often in word than in board
        for char in word:
            if word_count[char] > board_count[char]:
                return False
            
        # If first letter of word appears more than last, flip word to minimize no. of dfs
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]
        
        for row in range(self.row_num):
            for col in range(self.col_num):
                if self.dfs(word, row, col, set(), 0):
                    return True
        return False
    
    def dfs(self, word, row, col, visited, idx):
        if ((row, col) in visited 
            #Already found all chars we need
            or idx >= len(word) 
            #Out of bounds
            or row < 0 
            or col < 0 
            or row >= self.row_num
            or col >= self.col_num
            #Cell doesn't have the correct character
            or self.board[row][col] != word[idx]):
            return False
        #Cell holds last char of word
        elif idx == len(word) - 1 and word[idx] == self.board[row][col]:
            return True
        
        visited.add((row, col))
        if (self.dfs(word, row - 1, col, visited, idx + 1)
            or self.dfs(word, row + 1, col, visited, idx + 1)
            or self.dfs(word, row, col - 1, visited, idx + 1)
            or self.dfs(word, row, col + 1, visited, idx + 1)):
            return True
        visited.remove((row, col))                
        return False
    
#         qx= deque()
#         nrow = len(board)
#         ncol = len(board[0])
#         words = list(word)[::-1]
#         visited = dict()
#         ans=[]
        
        
                
#         def dfs(i,j,num):
#             if num==len(word):
#                 ans.append(1)
#                 return 
            
#             if 0<=i<nrow and 0<=j<ncol:
#                 if board[i][j]==word[num] and (i,j) not in visited:
#                     print(i,j,board[i][j])
#                     visited[(i,j)]=1
                    
#                     dfs(i-1,j,num+1)
#                     dfs(i,j-1,num+1)
#                     dfs(i,j+1,num+1)
#                     dfs(i+1,j,num+1)

                    

                
#         for i in range(nrow):
#             for j in range(ncol):
#                 dfs(i,j,0)
#                 visited=dict()
        
#         if ans:
#             return True
#         else:
#             return False
            