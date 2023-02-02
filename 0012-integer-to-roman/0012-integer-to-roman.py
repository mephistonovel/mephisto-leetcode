class Solution:
    def intToRoman(self, num: int) -> str:
        htable = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        
        nums = [*str(num)]
        length = len(nums)
        ans = deque()
        # i=0 -> 1 or 5
        # i=1 -> 10, 50
        # i=2 -> 100,500
        # i=3 -> 1000
        for i,n in enumerate(reversed(nums)):

            if n=='4': 
                ans.appendleft(htable[(10**i)*5])
                ans.appendleft(htable[10**i])
            elif n=='9':
                ans.appendleft(htable[(10**(i+1))])
                ans.appendleft(htable[(10**i)])
            elif n<'5':
                mod = int(n)%10
                char = htable[10**i]*mod
                ans.appendleft(char)
            elif n>='5':
                rest = int(n)-5 
                if rest == 0:
                    ans.appendleft(htable[(10**i)*5])
                else:
                    ans.appendleft(htable[(10**i)]*rest)
                    ans.appendleft(htable[(10**i)*5])
            else:
                #  n == '0'
                continue 
                    
                
        
        return ''.join(list(ans))