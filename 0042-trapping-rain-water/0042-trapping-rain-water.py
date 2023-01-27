class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(set(height)) <=1:
            return 0
        
        l = 0
        
        save = 0
        
        while height[l] == 0:
            l+=1 
        
        length = len(height)
        tmp_max = height[l]
        start = l+1
        rev = 0
        
        # l, r 을 앞에서부터 forward
        for r in range(start,len(height)):
  
            if height[r]>= tmp_max:
                l+=1
                while l!=r:
                    save += tmp_max - height[l]
                    l+=1
                tmp_max = height[r]
                rev = r
                print(save)
        
        if rev == length -1:
            return save
        
        # 한번 max나오면 이후로 안나오므로, 거꾸로 돌되 해당 max까지 돌게 함. 
        
        right = len(height)-1
        while height[right] == 0:
            right-=1
            
        rev_start = right
        tmp_max2 = height[right]

        for re in range(rev_start-1,rev-1,-1):
            if height[re]>=tmp_max2:
                right-=1

                while re != right:
                    save += tmp_max2 - height[right]
                    right-=1
                tmp_max2 = height[re]
                            
            
        
        return save
            
                
            
            
        