class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strlis=[]
        lenlis=[0]
        cpystr=list(s)
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        if len(s)==2:
            if s.count(s[0])==1:
                return 2
            return 1
        for i in range(0,len(s)):
            if s[i] not in strlis:
                cpystr+=s[i]
                strlis.append(s[i])
                isel=0
            else:
                isel=1
                lenlis.append(len(strlis))
                strlis=strlis[cpystr.index(s[i])+1:]
                cpystr=cpystr[cpystr.index(s[i])+1:]
                strlis.append(s[i])
        if isel==0:
            return max(len(strlis),max(lenlis))
        return max(lenlis)
                
        