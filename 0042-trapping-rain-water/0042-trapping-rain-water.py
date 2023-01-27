class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(set(height)) <=1:
            return 0
        
        l = 0
        
        save = 0
        
        while height[l] == 0:
            l+=1 
        
        print('l',l)
        length = len(height)
        tmp_max = height[l]
        start = l+1
        rev = 0
        print('tmp_max',tmp_max)
        
        for r in range(start,len(height)):
            # print(height[r]>=tmp_max)
            if height[r]>= tmp_max:
                print('l',l)
                print('r',r)
                l+=1
                while l!=r:
                    save += tmp_max - height[l]
                    l+=1
                tmp_max = height[r]
                rev = r
                print(save)
        
        if rev == length -1:
            return save
        
        
        right = len(height)-1
        while height[right] == 0:
            right-=1
            
        rev_start = right
        tmp_max2 = height[right]
        print(tmp_max2)
        print('rev',rev)
        for re in range(rev_start-1,rev-1,-1):
            if height[re]>=tmp_max2:
                right-=1
                # print(right)
                print('re',re)
                while re != right:
                    print('right',right)
                    save += tmp_max2 - height[right]
                    right-=1
                tmp_max2 = height[re]
                            
            
        
        return save
            
                
            
            
        