class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(0,n+1):
            val="{0:b}".format(int(i))
            val=str(val)
            res.append(val.count('1'))
        return res    
        