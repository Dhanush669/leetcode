class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a1=bin(int(a,2)+int(b,2))
        
        return str(a1[2:])       
                
                