class Solution:
    def myAtoi(self, s: str) -> int:
        is_negative=False
        alpha=['a',]
        intval=0
        is_positive=False
        intlis=[]    
        is_sined=False
        for i in range(0,len(s)):
            if len(intlis)>0 and not(intlis[0].isnumeric()):
                return 0
            if not(s[i].isnumeric()) and len(intlis)==0:
                if is_sined:
                    intlis.append(s[i])
                else:
                    if s[i]!='-' and s[i]!='+' and s[i]!=' ':
                        intlis.append(s[i])
            if intval>0 and not(s[i].isnumeric()):
                break    
            if s[i]. isnumeric():
                intval=(intval*10)+int(chr(ord(s[i])))
            if (not is_negative) and ((s[i]=='+') or (s[i].isnumeric() and int(chr(ord(s[i])))>=0)):    
                is_positive=True
                is_sined=True
            if (s[i]=='-') and (not is_positive):
                is_negative=True
                is_sined=True
        if is_negative:
            intval*=-1
        if intval < -2 ** 31:
            return -2147483648        
        if intval > 2 ** 31 - 1:
            return 2147483647
        return intval
        