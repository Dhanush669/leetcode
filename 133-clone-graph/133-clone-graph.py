"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
class Solution:
    
    def defa(self):
        return None
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node==None:
            return None
        
        dic=defaultdict(self.defa)
        nn=Node(node.val,[])
        queue=[node]
        visited=set()
        dic[node]=Node(node.val,[])
        while queue:
            t=queue[0]
            tval=t.val
            visited.add(t)
            newNode=dic[t]
            lis=[]
            for i in t.neighbors:
                if i not in visited:
                    queue.append(i)
                    dic[i]=Node(i.val,[])
                    visited.add(i)
                newNode.neighbors.append(dic[i])      
            
            del queue[0] 
            
        return dic[node] 
                    
        
        