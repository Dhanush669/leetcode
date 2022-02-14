#User function Template for python3
from collections import defaultdict
class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        dic=defaultdict(list)
        arr.sort()
        for i in range(1,len(arr)+1):
            #if i in arr:
            dic[arr[i-1]].append(arr[i-1])
            
        op=[]    
        first=False
        # for i in dic:
        #     #print(i,dic[i])
        #     if len(dic[i])>1:
        #         op.append(i)
        #         break
        
        for i in range(1,len(arr)+1):
            #print(i,dic[i])
            if len(dic[i])>1:
                op.append(i)
            if len(dic[i])==0:
                if len(op)==0:
                    first=True
                op.append(i)
            if len(op)==2:    
                break
        
        # for i in range(1,len(arr)+1):
        #     #print(i,dic[i])
        #     if len(dic[i])==0:
        #         op.append(i)
        #         break
        if first:
            return op[::-1]
        return op   

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends