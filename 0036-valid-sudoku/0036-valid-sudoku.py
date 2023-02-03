class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 어케 해시로 풀지?
        # or set? -> in operator가 O(1)임을 이용
        #https://leetcode.com/problems/valid-sudoku/discuss/2567887/C%2B%2B-Easy-solution-using-vector-set #
        r = collections.defaultdict(set)
        c = collections.defaultdict(set)
        inner = collections.defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                curr = board[i][j]
                if (curr in r[i]) or (curr in c[j]) or (curr in inner[(i//3)*3+j//3]):
                    return False
                
                r[i].add(curr)
                c[j].add(curr)
                inner[(i//3)*3+j//3].add(curr)
        
        return True
        

#### naive 풀이 ###### 45.79%, 75.93%
#         # 가로줄
#         # check(board)
#         for garo in board:
#             nums = set(garo)-set('.')
#             garos = [n for n in garo if n!='.']
#             if len(garos)>len(nums):
#                 return False
        
#         # inner box
#         tmp_num = []
#         for i in range(3):
#             tmp = board[3*i:3*(i+1)] # board[0:3]
#             # tmp[0,0] ~ tmp[2,2]
#             # tmp[0,3] ~ tmp[2,5]
#             # tmp[0,6] ~ tmp[2,8]
#             for j in range(3):
#                 tmp_num = [tmp[0][3*j],tmp[0][3*j+1],tmp[0][3*j+2],tmp[1][3*j],tmp[1][3*j+1],tmp[1][3*j+2], tmp[2][3*j], tmp[2][3*j+1],tmp[2][3*j+2]]
#                 tmp_num2 = [n for n in tmp_num if n!= '.']
#                 nums = set(tmp_num)-set('.')
#                 # print(nums)
#                 if len(tmp_num2)>len(nums):
#                     return False
            
        
        
#         # 세로줄
#         self.transpose(board)
        
#         for sero in board:
#             nums = set(sero)-set('.')
#             seros = [n for n in sero if n!='.']
#             if len(seros)>len(nums):
#                 return False
        
#         return True
        
    
#     def transpose(self,board):
#         for i in range(9):
#             for j in range(i+1,9):
#                 board[i][j] , board[j][i] = board[j][i], board[i][j]
        
        