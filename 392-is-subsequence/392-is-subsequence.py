class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pos=[]
        f=0
        #print(t.index('t'),t.index('w'),t.index('n'))
        for i in s:
            if i not in t:
                return False
            
            if len(pos)==0:
                pos.append(t.index(i))
            else:
                pos.append(t.index(i)+f)
            f+= len(t[:t.index(i)])  +1  
            t=t[t.index(i)+1:]
        #print(pos)    
        for i in range(0,len(pos)-1)    :
            if pos[i]>pos[i+1]:
                return False
        return True    
        