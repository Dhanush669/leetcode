#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def DFS(self,node,adj,visited,op):
        visited.add(node)
        op.append(node)
        for adjacent in adj[node]:
            if adjacent not in visited:
                op=self.DFS(adjacent,adj,visited,op)
        return op        
                
    def dfsOfGraph(self, V, adj):
        # code here
        visited=set()
        return self.DFS(0,adj,visited,[])
        

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends