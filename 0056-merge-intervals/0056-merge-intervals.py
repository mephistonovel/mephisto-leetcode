class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals 
        
        ## sorting based on the first element of each element ##
        # https://www.daleseo.com/sort-merge/ 
        def mergesort(nlist):
            def sort(low, high):
                if high-low>=2:
                    mid = (high+low)//2
                    sort(low,mid)
                    sort(mid,high)
                    merge(low,mid,high)         
                    
            def merge(l,m,h):
                tmp = []
                i=l
                j=m
                while i<m and j<h:
                    if nlist[i][0] < nlist[j][0]:
                        tmp.append(nlist[i])
                        i+=1
                    elif nlist[i][0] > nlist[j][0]:
                        tmp.append(nlist[j])
                        j+=1
                    else:
                        if nlist[i][1] < nlist[j][1]:
                            tmp.append(nlist[i])
                            i+=1
                        else:
                            tmp.append(nlist[j])
                            j+=1
                while i<m:
                    tmp.append(nlist[i])
                    i+=1
                while j<h:
                    tmp.append(nlist[j])
                    j+=1
                
                # print(tmp)
                
                for r in range(l,h):
                    nlist[r] = tmp[r-l]
            return sort(0,len(nlist))
    
    
        mergesort(intervals)
        
        # print(intervals)
            
        ## after sorting
        tmp_low = intervals[0][0]
        tmp_end = intervals[0][1]
        ans = []
        
        for i in range(1,len(intervals)):
            low = intervals[i][0]
            end = intervals[i][1]
            
            if tmp_low<=low<=tmp_end and end>=tmp_end:
                if not ans or ans[-1][0]!=tmp_low:
                    ans.append([tmp_low,end])
                if ans and ans[-1][0]==tmp_low:
                    ans.pop()
                    ans.append([tmp_low,end])
                    
                tmp_end = end
                
            elif tmp_low<=low<=tmp_end and end<tmp_end:
                if not ans or ans[-1][0]!=tmp_low:
                    ans.append([tmp_low,tmp_end])
                if ans and ans[-1][0]==tmp_low:
                    ans.pop()
                    ans.append([tmp_low,tmp_end])
                    
            
            else:
                if not ans:
                    ans.append([tmp_low,tmp_end])
                ans.append([low,end])
            
                tmp_low = low
                tmp_end = end
            
        return ans
        