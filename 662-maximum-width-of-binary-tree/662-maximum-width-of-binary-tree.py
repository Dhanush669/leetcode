# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    
    def level(self,root,dic,l,posi):
        if root==None:
            return
        
        dic[l].append(posi)        
        self.level(root.left,dic,l+1,posi*2)
        self.level(root.right,dic,l+1,(posi*2+1))
        return dic
    
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic=defaultdict(list)
        dic=self.level(root,dic,1,1)
        maxi=0
        for i in dic:
            t=(max(dic[i])-min(dic[i]))+1
            if t>maxi:
                maxi=t
        return maxi        
            
        