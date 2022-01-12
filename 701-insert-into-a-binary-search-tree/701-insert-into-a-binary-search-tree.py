# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def Insert(root,val):
    if root==None:
        newNode=TreeNode(val,None,None)
        root=newNode
    elif val>root.val:
        root.right=Insert(root.right,val)
        
    else:
        root.left=Insert(root.left,val)
        
    return root    
        
            

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return Insert(root,val)

            
        