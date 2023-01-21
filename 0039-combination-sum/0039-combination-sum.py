class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #corner case
        if min(candidates)>target:
            return []
        
        ans = []
        tmp = []
        
        candidates.sort()
        
        def part(start,tmp,sum_sofar):
            if sum_sofar==target:
                ans.append(tmp[:])
                return 
            elif sum_sofar>target:
                return
            else:
                for i in range(start,len(candidates)):
                    num = candidates[i]
                    tmp.append(num)
                    sum_sofar+= num
                    part(i, tmp,sum_sofar)
                    sum_sofar-= num
                    
                    tmp.pop()
        
        part(0,[],0)
                
            
        
        return ans
            
#         for num in cnadidates:
#             #rem target
#             rem = target - num
            
            