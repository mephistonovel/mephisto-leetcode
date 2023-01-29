class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n==2 or n==3:
            return []
        if n==1:
            return [["Q"]]
        
        ##참고: https://www.fun-coding.org/Chapter21-backtracking-live.html#gsc.tab=0
        
        ans = []

        cand = [i for i in range(n)]

        def check(tmp,new_num):
            if not tmp: #비어있으면 채워넣을 때 
                return True
            else:
                current_row = len(tmp) # 현재 row는 tmp의 다음타자애 -> len(tmp)
                for qrow in range(current_row):
                    if abs(tmp[qrow]-new_num) == current_row-qrow: #대각선...
                        return False
                return True

        tmp = []
        tmp_char = []
        
        def dfs(rest,tmp,tmp_char):
            if len(tmp)==n:
                ans.append(tmp_char[:])
                return

            for i in rest:
                if check(tmp,i):
                    char = '.'*i + 'Q'+'.'*(n-1-i)
                    
                    tmp.append(i)
                    tmp_char.append(char)
                    
                    new_rest = list(set(rest)-set(tmp))
                    
                    dfs(new_rest,tmp,tmp_char)
                    
                    tmp.pop()
                    tmp_char.pop()
            
        dfs(cand,[],tmp_char)
        
        return ans
    
                

        
        

                
                
        

        
        