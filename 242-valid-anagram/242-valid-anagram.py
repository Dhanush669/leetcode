from collections import defaultdict
class Solution:
    def defu(self):
        return 0
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sset=defaultdict(self.defu)
        tset=defaultdict(self.defu)
        for i in range(0,len(s)):
            sset[s[i]]+=1
            tset[t[i]]+=1
        if sset==tset:
            print(sset,tset)
            return True
        return False
        