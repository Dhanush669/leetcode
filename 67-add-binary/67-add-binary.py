class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # a1=bin(int(a,2)+int(b,2))
        # return str(a1[2:])       
        a1=a[::-1]        
        b1=b[::-1]
        carry='0'
        res=""
        while len(a1)!=0 or len(b1)!=0:
            su=""
            if len(a1)>0:
                x=a1[0]
                a1=a1[1:]
            else:
                x='0'
            if len(b1)>0:
                y=b1[0]
                b1=b1[1:]
            else:
                y='0'
            if x=='1' and y=='1':
                su='0'
                if carry!='0':
                    su='1'
                carry='1'    
            elif (x=='1' and y=='0') or (y=='1' and x=='0'):
                su='1'
                if carry!='0':
                    su='0'
                    carry='1'    
            else:
                if carry!='0':
                    su='1'
                    carry='0'
                else:
                    su='0'
            res+=su
            
        if carry!='0'    :
            res+='1'
        return res[::-1]    
                