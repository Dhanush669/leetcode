class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a1=a[::-1]
        b1=b[::-1]
        res=""
        carry="0"
        a1=bin(int(a,2)+int(b,2))
        
        return str(a1[2:])       
                
                