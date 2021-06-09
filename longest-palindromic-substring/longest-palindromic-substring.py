class Solution:
    def longestPalindrome(self, s: str) -> str:
        pallis=[s[0]]
        cpystr=""
        for i in range(0,len(s)):
            si=s[i:]
            if si.count(si[0])>1 and len(si)>len(pallis[0]):
                for j in si:
                    cpystr+=j
                    if cpystr==cpystr[::-1]:
                        if len(cpystr)>len(pallis[0]):
                            pallis[0]=cpystr
            cpystr=""    
                    
        return pallis[0]