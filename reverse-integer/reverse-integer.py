class Solution:
    def reverse(self, x: int) -> int:
        is_negative=False
        cpy=x
        if x>0 and x<10:
            return x
        sum1=0
        if x<0:
            
            if x>-10:
                return x
            x*=-1
            is_negative=True
        r=0    
        while(x>0):
            r=x%10
            sum1=sum1*10+r
            x=x//10
        if sum1 < -2 ** 31 or sum1 > 2 ** 31 - 1:
            return 0
        # return sum1    
        if is_negative:
            
            return -1*sum1
        return sum1
            
            
        