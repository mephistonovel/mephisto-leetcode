class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r = collections.defaultdict(set)
        c = collections.defaultdict(set)
        inner = collections.defaultdict(set)
        blank = []
        # nums = {1,2,3,4,5,6,7,8,9}
        # cand = [set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                tmp = board[i][j]
                if tmp != '.':
                    r[i].add(tmp)
                    c[j].add(tmp)
                    inner[(i//3)*3+j//3].add(tmp)
                else:
                    blank.append((i,j))
        
        def dfs(bl_idx):
            if bl_idx >= len(blank):
                return True
            
            row,col = blank[bl_idx]
            for cand in '123456789':
                if (cand not in r[row]) and (cand not in c[col]) and (cand not in inner[(row//3)*3+col//3]):
                    r[row].add(cand)
                    c[col].add(cand)
                    inner[(row//3)*3+col//3].add(cand)
                    board[row][col] = cand
                    
                    if dfs(bl_idx+1):
                        return True
                    else:
                        r[row].remove(cand)
                        c[col].remove(cand)
                        inner[(row//3)*3+col//3].remove(cand)
                        board[row][col] = '.'
            
            return False
        
        dfs(0)  
        
        return board
                # if tmp=='.':
                #     cand_ = r[i] | c[j]
                #     cand_ = cand_ | inner[(i/3)*3+j/3]
                #     if len(nums-cand_)==1:
                #         board[i][j] = list(nums-cand_)[0]
                    

        