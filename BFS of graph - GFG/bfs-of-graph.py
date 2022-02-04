#User function Template for python3

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        visited=set()
        queue=[]
        BFS=[]
        queue.append(0)
        visited.add(0)
        while len(queue)>0:
            BFS.append(queue[0])
            for adjacent in adj[queue[0]]:
                if adjacent not in visited:
                    visited.add(adjacent)
                    queue.append(adjacent)
            del queue[0]        
        return BFS    

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends