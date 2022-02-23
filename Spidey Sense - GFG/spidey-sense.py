from collections import defaultdict
class Solution:
    def __init__(self):
        self.op=[]
        
    def helper(self,matrix,m,n,i,j,prev):
        if ((i<0 or i>=m) or (j>=n or j<0)) or (matrix[i][j]=='W' or matrix[i][j]=='B') or(self.op[i][j]>0):
            return []
        t=prev+1
        if self.op[i][j]!=-1:
            if t<self.op[i][j]:
                self.op[i][j]=t
        else:
            self.op[i][j]=t
        return [i,j]    
        
        
    def findDistance(self, matrix, m, n):
        # Your code goes here
        dic=defaultdict(list)
        lis=[]
        self.op=[]
        for i in range(0,m):
            t=[]
            for j in range(0,n):
                t.append(-1)
            self.op.append(t)    
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j]=='B':
                    self.op[i][j]=0
                    lis.append([i,j])
        #print(lis)            
        while lis:
            t=lis[0]
            i=t[0]
            j=t[1]

            o=self.helper(matrix,m,n,i-1,j,self.op[i][j])
            if len(o)>0:
                lis.append(o)
            o=self.helper(matrix,m,n,i,j-1,self.op[i][j])
            if len(o)>0:
                lis.append(o)
            o=self.helper(matrix,m,n,i+1,j,self.op[i][j])
            if len(o)>0:
                lis.append(o)
            o=self.helper(matrix,m,n,i,j+1,self.op[i][j])
            if len(o)>0:
                lis.append(o)
                
            del lis[0]
        
        
        return self.op




#{ 
#  Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        size = input().strip().split()
        m = int(size[0])
        n = int(size[1])
        matrix=[]
        for _ in range(m):
            matrix.append( [ x for x in input().strip().split() ] )
        obj = Solution() 
        result = obj.findDistance(matrix,m,n)
        for i in result:
            for j in i:
                print(j, end=' ')
            print()
# } Driver Code Ends