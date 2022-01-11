# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
lis=[]
def getSum(oroot,root,val):
    if root==None:
        return
    val+=str(root.val)
    res=0

    res=getSum(oroot,root.left,val)
    if res!=None:
        lis.append(res)  
    res=getSum(oroot,root.right,val)    
    if res!=None:
        lis.append(res)
    
    if root.left!=None or root.right!=None:
        return
    return val


class Solution:
    
        
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        su=0
        
        c=getSum(root,root,"")
        print(lis)
        m=0
        # for i in lis:
        #     if len(i)>m:
        #         m=len(i)
        for i in lis:
            
            su+=int(i,2)
        l=len(lis)    
        for i in range(0,l):
            del lis[0]
        print(lis)    
        if l==0:
            return int(c)
        return su