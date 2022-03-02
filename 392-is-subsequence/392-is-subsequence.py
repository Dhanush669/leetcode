class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #pos=[]
        pre=0
        f=0
        #print(t.index('t'),t.index('w'),t.index('n'))
        for i in s:
            if i not in t:
                return False
            if pre==0:
                pre=t.index(i)
            else:
                pre=t.index(i)+f
            # if len(pos)==0:
            #     pos.append(t.index(i))
            # else:
            #     pos.append(t.index(i)+f)
            f+= len(t[:t.index(i)])  +1
            if f<pre:
                return False
            t=t[t.index(i)+1:]
        return True    
        