#User function Template for python3

class Solution:
    
    def Isprime(self,n):
        if n==2 or n==3:
            return n
        for i in range(2,n//2)    :
            if n%i==0:
                return False
        return True        
    
    def primeDivision(self, N):
        # code here
        prime=[]
        # for i in range(4,N+1):
        #     flag=True
        #     for j in range(2,(i//2)+1):
        #         if i%j==0:
        #             flag=False
        #             break
        #     if flag:
        #         prime.append(i)
        # for i in prime:
        #     if (N-i) in prime:
        #         return[i,(N-i)]
        for i in range(2,N+1):
            if self.Isprime(i):
                if self.Isprime(N-i):
                    return [i,(N-i)]
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        p1, p2 = ob.primeDivision(N)
        print(p1,end=" ")
        print(p2)
# } Driver Code Ends