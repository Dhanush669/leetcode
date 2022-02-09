#User function Template for python3
from collections import defaultdict
class Solution:
    def sortBySetBitCount(self, arr, n):
        # Your code goes here
        graph=defaultdict(list)
        for i in arr:
            t=str(bin(i).replace("0b", ""))
            c=t.count('1')
            graph[c].append(i)
        ind=0
        for key,value in sorted(graph.items(),reverse=True):
            for i in value:
                arr[ind]=i
                ind+=1
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortBySetBitCount(arr, n)
        print(*arr)

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends